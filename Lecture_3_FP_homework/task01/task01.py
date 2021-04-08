# Using functional approach, generators, currying,
# implement functions that writes IP list of redirected requests (code 304) into another file
# separate pure_func from functions that change state (io_func)
# write negative test "test_myfunc_negative"
# Set pytest as default runner https://stackoverflow.com/questions/6397063/how-do-i-configure-pycharm-to-run-py-test-tests
# hit Ctrl+Shift+F10 or RMB on the file to run tests

def io_func(logfile_path, result_file_path):
    with open(logfile_path, "r") as data, open(result_file_path, "w") as result:
        all_lines = data.readlines()
        lines_with_redirect = filter(lambda x: x is not None, list(map(pure_func, all_lines)))
        result.write(chr(10).join(lines_with_redirect))


def pure_func(file_line):
    if file_line.find("HTTP/1.1\" 304") != -1:
        return file_line.split(" ")[0]


def test_myfunc_positive():
    line = '218.30.103.62 - - [17/May/2015:11:05:17 +0000] "GET /projects/xdotool/xdotool.xhtml \
    HTTP/1.1" 304 - "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"'
    assert pure_func(line) == "218.30.103.62"


def test_myfunc_negative():
    line = '83.149.9.216 - - [17/May/2015:10:05:03 +0000] ' \
           '"GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1" 200 203023 ' \
           '"http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; ' \
           'Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"'
    assert pure_func(line) is None


def test_real_file():
    io_func("apache_log", "redirect_hosts.txt")