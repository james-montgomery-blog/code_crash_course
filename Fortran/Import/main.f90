program addNumbers

   use :: mymath

! Type declarations
   real :: a, b, result

! Executable statements
   a = 12.0
   b = 15.0
   result = add(a, b)
   print *, 'The total is ', result

end program addNumbers
