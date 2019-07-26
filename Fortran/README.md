# Fortran

## History

Fortran is a general-purpose, compiled imperative programming language that is especially suited to numeric computation and scientific computing. Originally developed by IBM in the 1950s for scientific and engineering applications, FORTRAN came to dominate this area of programming early on and has been in continuous use for over six decades in computationally intensive areas such as numerical weather prediction, finite element analysis, computational fluid dynamics, computational physics, crystallography and computational chemistry. It is a popular language for high-performance computing and is used for programs that benchmark and rank the world's fastest supercomputers.

## Installation

Similarly to C, you very rarely need to install Fortran if you are using a modern operating system.

If you don't already have it, you can install the compiler using brew:

```
brew install gcc
```

## HelloWorld

We'll use the `.f90` file extension instead of `.f95` so that our compiled files share the `a.out` naming convention of the `C` languages.

```
gfortran -o hello ./HelloWorld/HelloWorld.f90
./a.out
```

<!--
* https://www.tutorialspoint.com/fortran/fortran_arrays.htm
-->

# Imports

```
gfortran ./Import/main.f90 ./Import/utils.f90
./a.out
```
