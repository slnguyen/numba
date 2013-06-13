import numpy as np
from ..compiler import compile
from ..types import *
from .support import testcase, main

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def floordiv(a, b):
    return a // b

def mod(a, b):
    return a % b

iset = [int8, int16, int32, int64, uint8, uint16, uint32, uint64]
fset = [float32, float64]
cset = [complex64, complex128]

#------------------------------------------------------------------------------
# add

@testcase
def test_add_integer():
    def run(ty, a, b):
        cadd = compile(add, ty, [ty, ty])
        got = cadd(a, b)
        exp = add(a, b)
        assert got == exp, 'add(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in iset:
        run(ty, 12, 34)


@testcase
def test_add_float():
    def run(ty, a, b):
        cadd = compile(add, ty, [ty, ty])
        got = cadd(a, b)
        exp = add(a, b)
        assert np.allclose(got, exp), 'add(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in fset:
        run(ty, 1.234, 2.345)


@testcase
def test_add_complex():
    def run(ty, a, b):
        cadd = compile(add, ty, [ty, ty])
        got = cadd(a, b)
        exp = add(a, b)
        assert np.allclose(got, exp), 'add(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in cset:
        run(ty, 1.2+34j, 2.4+56j)

#------------------------------------------------------------------------------
# sub

@testcase
def test_sub_integer():
    def run(ty, a, b):
        csub = compile(sub, ty, [ty, ty])
        got = csub(a, b)
        exp = sub(a, b)
        assert got == exp, 'sub(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in iset:
        run(ty, 45, 12)


@testcase
def test_sub_float():
    def run(ty, a, b):
        csub = compile(sub, ty, [ty, ty])
        got = csub(a, b)
        exp = sub(a, b)
        assert np.allclose(got, exp), 'sub(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in fset:
        run(ty, 1.234, 2.345)


@testcase
def test_sub_complex():
    def run(ty, a, b):
        csub = compile(sub, ty, [ty, ty])
        got = csub(a, b)
        exp = sub(a, b)
        assert np.allclose(got, exp), 'sub(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in cset:
        run(ty, 1.2+34j, 2.4+56j)

#------------------------------------------------------------------------------
# mul

@testcase
def test_mul_integer():
    def run(ty, a, b):
        cmul = compile(mul, ty, [ty, ty])
        got = cmul(a, b)
        exp = mul(a, b)
        assert got == exp, 'mul(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in iset:
        run(ty, 2, 3)

@testcase
def test_mul_float():
    def run(ty, a, b):
        cmul = compile(mul, ty, [ty, ty])
        got = cmul(a, b)
        exp = mul(a, b)
        assert np.allclose(got, exp), 'mul(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in fset:
        run(ty, 1.234, 2.345)

#------------------------------------------------------------------------------
# div

@testcase
def test_div_integer():
    def run(ty, a, b):
        cdiv = compile(div, ty, [ty, ty])
        got = cdiv(a, b)
        exp = div(a, b)
        assert got == exp, 'div(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in iset:
        run(ty, 4, 2)

@testcase
def test_div_float():
    def run(ty, a, b):
        cdiv = compile(div, ty, [ty, ty])
        got = cdiv(a, b)
        exp = div(a, b)
        assert np.allclose(got, exp), 'div(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in fset:
        run(ty, 1.234, 2.345)


#------------------------------------------------------------------------------
# floordiv

@testcase
def test_floordiv_integer():
    def run(ty, a, b):
        cfloordiv = compile(floordiv, ty, [ty, ty])
        got = cfloordiv(a, b)
        exp = floordiv(a, b)
        assert got == exp, 'floordiv(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in iset:
        run(ty, 4, 2)

@testcase
def test_floordiv_float():
    def run(ty, a, b):
        cfloordiv = compile(floordiv, ty, [ty, ty])
        got = cfloordiv(a, b)
        exp = floordiv(a, b)
        assert got == exp, 'floordiv(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in fset:
        run(ty, 1.234, 2.345)



#------------------------------------------------------------------------------
# mod

@testcase
def test_mod_integer():
    def run(ty, a, b):
        cmod = compile(mod, ty, [ty, ty])
        got = cmod(a, b)
        exp = mod(a, b)
        assert got == exp, 'mod(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in iset:
        run(ty, 121, 11)

@testcase
def test_mod_float():
    def run(ty, a, b):
        cmod = compile(mod, ty, [ty, ty])
        got = cmod(a, b)
        exp = mod(a, b)
        assert got == exp, 'mod(%s, %s) got = %s expect=%s' % (a, b, got, exp)

    for ty in fset:
        run(ty, 432., 21.)


if __name__ == '__main__':
    main()

