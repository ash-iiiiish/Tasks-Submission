class Calculator:
    def add(self,a,b):
        return a+b  
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
    def power(self,a,b):
        return a**b
    def modulus(self,a,b):
        return a%b
    def floor_divide(self,a,b):
        return a//b
    def square_root(self,a):
        return a**0.5
    def cube_root(self,a):
        return a**(1/3)
    def percentage(self,a,b):
        return (a/b)*100
    def factorial(self,a):
        if a==0 or a==1:
            return 1
        else:
            fact=1
            for i in range(2,a+1):
                fact=fact*i
            return fact
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a

    def lcm(self,a,b):
        return abs(a*b)//self.gcd(a,b)
    def is_prime(self,a):
        if a<=1:
            return False
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
        return True
    def fibonacci(self,n):
        fib_sequence=[]
        a,b=0,1
        for _ in range(n):
            fib_sequence.append(a)
            a,b=b,a+b
        return fib_sequence
    def factorial_recursive(self,a):
        if a==0 or a==1:
            return 1
        else:
            return a*self.factorial_recursive(a-1)
    def sum_of_natural_numbers(self,n):
        return n*(n+1)//2
    def average(self,nums):
        return sum(nums)/len(nums)
    def max_in_list(self,nums):
        return max(nums)
    def min_in_list(self,nums):
        return min(nums)
    def reverse_number(self,a):
        rev=0
        while a>0:
            digit=a%10
            rev=rev*10+digit
            a=a//10
        return rev
    def is_palindrome(self,a):
        return str(a)==str(a)[::-1]
    def decimal_to_binary(self,a):
        return bin(a).replace("0b","")
    def binary_to_decimal(self,a):
        return int(a,2)
    def decimal_to_octal(self,a):
        return oct(a).replace("0o","")
    def octal_to_decimal(self,a):
        return int(a,8)
    def decimal_to_hexadecimal(self,a):
        return hex(a).replace("0x","")
    def hexadecimal_to_decimal(self,a):
        return int(a,16)
    def lcm_of_list(self,nums):
        from functools import reduce
        def lcm(a,b):
            return abs(a*b)//self.gcd(a,b)
        return reduce(lcm,nums)
    def gcd_of_list(self,nums):
        from functools import reduce
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        return reduce(gcd,nums)
    def sum_of_squares(self,n):
        return sum(i**2 for i in range(1,n+1))
    def sum_of_cubes(self,n):
        return sum(i**3 for i in range(1,n+1))
    def harmonic_number(self,n):
        if n<=0:
            return 0
        return sum(1/i for i in range(1,n+1))
    def collatz_sequence(self,n):
        sequence=[n]
        while n!=1:
            if n%2==0:
                n=n//2
            else:
                n=3*n+1
            sequence.append(n)
        return sequence
    def digit_sum(self,a):
        total=0
        while a>0:
            total+=a%10
            a=a//10
        return total
    def digit_count(self,a):
        count=0
        while a>0:
            count+=1
            a=a//10
        return count
    def is_armstrong(self,a):

        
        num_str=str(a)
        num_len=len(num_str)
        total=sum(int(digit)**num_len for digit in num_str)
        return total==a

    def collatz_steps(self,n):
        steps=0
        while n!=1:
            if n%2==0:
                n=n//2
            else:
                n=3*n+1
            steps+=1
        return steps
    def pascal_triangle(self,rows):
        triangle=[]
        for i in range(rows):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=triangle[i-1][j-1]+triangle[i-1][j]
            triangle.append(row)
        return triangle
    def sum_of_digits(self,a):
        return sum(int(digit) for digit in str(a))
    def product_of_digits(self,a):
        product=1
        for digit in str(a):
            product*=int(digit)
        return product
    def is_perfect_number(self,a):
        if a<2:
            return False
        divisors_sum=sum(i for i in range(1,a) if a%i==0)
        return divisors_sum==a
    def abundant_number(self,a):
        if a<12:
            return False
        divisors_sum=sum(i for i in range(1,a) if a%i==0)
        return divisors_sum>a
    def deficient_number(self,a):
        if a<1:
            return False
        divisors_sum=sum(i for i in range(1,a) if a%i==0)
        return divisors_sum<a
    def collatz_max(self,n):
        max_value=n
        while n!=1:
            if n%2==0:
                n=n//2
            else:
                n=3*n+1
            if n>max_value:
                max_value=n
        return max_value
    def is_strong_number(self,a):
        def factorial(num):
            if num==0 or num==1:
                return 1
            fact=1
            for i in range(2,num+1):
                fact=fact*i
            return fact
        total=sum(factorial(int(digit)) for digit in str(a))
        return total==a

    def sum_of_even_numbers(self,n):
        return sum(i for i in range(2,n+1,2))
    def sum_of_odd_numbers(self,n):
        return sum(i for i in range(1,n+1,2))
    def reverse_list(self,nums):
        return nums[::-1]
    def is_circular_prime(self,a):
        def is_prime(num):
            if num<=1:
                return False
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    return False
            return True
        str_num=str(a)
        for i in range(len(str_num)):
            rotated_num=int(str_num[i:]+str_num[:i])
            if not is_prime(rotated_num):
                return False
        return True
