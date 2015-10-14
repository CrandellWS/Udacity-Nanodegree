## http://stackoverflow.com/a/31367197/1815624

    class Outer(object):
        def __init__(self, outer_num):
            self.outer_num = outer_num

        def create_inner_class(outer_self, inner_arg):
            class Inner(object):
                outer_self.inner_arg = inner_arg
                def weird_sum_with_closure_scope(inner_self, num):
                    return num + outer_self.outer_num + inner_arg
            return Inner
o = Outer(3).create_inner_class(4)().weird_sum_with_closure_scope(5)
print(o)


## now that is something to think about
