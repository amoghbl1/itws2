import sys

def collect_fun_defs(inp):
    def func_body_begin(s):
        return s == '{\n' or s == '{ \n'

    def func_body_close(s):
        return s == '}\n' or s == '} \n'

    fun_heads = []
    prev_line = None
    fun_head = None

    for line in inp:
        if func_body_begin(line):
            fun_head = prev_line
            for line in inp:
                if func_body_close(line):
                    assert(fun_head is not None)
                    fun_head = fun_head.strip()
                    fun_heads.append(fun_head)
                    fun_head = None
                    break
        prev_line = line
    
    return fun_heads


"This program is not meant to be imported and reused!"
"Launch this program from the command line"
try:
    if len(sys.argv) != 2:
	    #sys.stderr.writelines(["usage: fc <filepath>", "\n"])
	    #sys.exit(1)
	    f = sys.stdin
    else:
        f = open(sys.argv[1])
except IOError:
	sys.stderr.writelines(["Error: failed to open '", sys.argv[1], "'. Quitting...\n"])
else:
    funs = collect_fun_defs(f)
    f.close()
    for head in funs:
    	print head






