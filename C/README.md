# C

## History

C was originally developed at Bell Labs by Dennis Ritchie between 1972 and 1973 to make utilities running on Unix.  It is one of the most widely used programming languages, with C compilers from various vendors available for the majority of existing computer architectures and operating systems. C is an imperative procedural language. It was designed to be compiled using a relatively straightforward compiler, to provide low-level access to memory, to provide language constructs that map efficiently to machine instructions, and to require minimal runtime support.

C provides efficiency, high performance, and high quality softwares, flexibility and power, many high-level and low-level operations like middle level, stability and small size code, provide functionality through rich set of function libraries, and gateway for other professional languages like C, C++, and Java.

## Installation

You don't need to install C. C is an amazingly low-level, powerful language that almost any computer you will ever use leverages.

If you don't already have it, you can install the compiler using brew:

```
brew install gcc
```

## HellowWorld

```
gcc ./HelloWorld/HelloWorld.c
./a.out
```

## Import

```
gcc ./Import/main.c
./a.out
```

## OLS

<!--
https://pheiter.wordpress.com/2012/09/04/howto-installing-lapack-and-blas-on-mac-os/

https://kevincodeidea.wordpress.com/2015/03/12/install-cblas-on-yosemite/
-->

We will need a linear algebra library to help with our ordinary least squares regression. We'll use Blas and CBlas.

**Install [BLAS](http://www.netlib.org/blas/):**

```
tar -xvzf ./OLS/blas-3.8.0.tgz -C ./OLS
cd ./OLS/BLAS-3.8.0
make
mv blas_LINUX.a libblas.a
cp libblas.a /usr/local/lib/
```

and clean up...

```
cd ../..
rm -r ./OLS/BLAS-3.8.0
```

**Install CBLAS:**

<!--
BLAS docs
http://www.netlib.org/blas/dgemm.f
https://software.intel.com/en-us/mkl-developer-reference-c-cblas-gemm
-->

```
tar -xvzf ./OLS/cblas.tgz -C ./OLS
cd ./OLS/CBLAS
nano Makefile.in
```

Update the following lines in `Makefile.in`:

```
BLLIB = /usr/local/lib/libblas.a
CBLIB = ../lib/cblas_$(PLAT).a
```

```
make
cp include/* /usr/local/include/
cp lib/cblas_LINUX.a /usr/local/lib/
```

<!--
files moved to /usr/local/lib/

cblas.h		
cblas_f77.h
-->

<!--
test cblas

gcc -lcblas -I/usr/local/include ./OLS/CBLAS/examples/cblas_example1.c
-->

and clean up...

```
cd ../..
rm -r ./OLS/CBLAS
```

**Run the Code!**

Now that we have BLAS and CBLAS installed, we can run our code.

```
make --directory ./OLS && mv ./OLS/main ./main
./main
```

```
gcc -lcblas -I/usr/local/include ./OLS/src/main.c
./a.out
```
