# Unit-Tests
Unit testing practice, going from simple programs to more complex ones.  
This README is a 'journal' which I am using to help me learn about unit testing.
## Double
With the function double, which simply doubles a given number, I am testing both if the function works perfectly and if the function does not work perfectly.
This way, I can see how the errors given from the test can help me debug the and discover the problem.
### Testing without pytest
#### Testing without addition error
The function correctly doubles a number. 
I am testing 2 and 3 as shown below:  
![image](https://github.com/user-attachments/assets/f060e73d-a803-4ff0-a5df-9b57e5fab7b8)  
Running `test_calculator.py` gave me nothing meaning that no errors occurred.  
![image](https://github.com/user-attachments/assets/73dfd7ea-8602-49b5-aa86-58db699aa7ba)  
#### Testing with addition error
The error is that the double function adds 2 to the given number rather than multiplying it by 2.  
![image](https://github.com/user-attachments/assets/1f6a3fa7-4800-4b2a-9fd5-0fa0b55ee553)  
Running `test_calculator.py`, it gave this error:  
![image](https://github.com/user-attachments/assets/b6f36d54-e2e8-4c97-9681-dd0aa415c1c5)  
This means that the test failed at the `assert double(3) == 6`, meaning that when 3 is currently passed into this version of double, the output is not 6.  
However, the test was successful at `assert double(2) == 4`. This is a coincidence since 2*2=4 and 2+2=4.  
Therefore, this prompts me to look at my double function and see that it has a logical error, allowing me to fix it.  
The tests give me clues on what the error could be (if there is one) so therefore it must be more efficient to use all types of tests (such as valid, invalid, boundary, erroneous) rather than only multiple tests of one type as it will allow me to narrow down the error quicker, saving time.

#### Multiple tests
If I still cannot find the error I may want more clues to narrow it down. Therefore it is important that I am able to do multiple tests and see each of their results.  
Therefore, I am testing 0 after testing 2 and 3 (which should fail with the addition error and should succeed without the addition error).  
![image](https://github.com/user-attachments/assets/c2c54f8d-b077-4320-b817-53c066ed769a)  
##### Without addition error  
Running `python test_calculator.py` to make sure 0 succeeds, it outputs nothing:  
![image](https://github.com/user-attachments/assets/66e3751a-75a5-4805-8ea9-cef576557068)  
Therefore 0 is successful
##### With addition error
Running `python test_calculator.py`, it gives this output:  
![image](https://github.com/user-attachments/assets/ac92f088-5ebe-4dfa-8914-ce3168965351)  
Showing that the program only tests up to 3 (up to the first failed test).  
Therefore, to get around this issue, I will put tests in separate functions.  
![image](https://github.com/user-attachments/assets/810b5a59-23f0-40b3-8570-945440a34c70)  
Running `python test_calculator.py`, it gives this output:  
![image](https://github.com/user-attachments/assets/40217480-215d-46ee-9a79-015d2f33f032)  
It did not test them all. Therefore, I will use the `try` and `except` keywords in Python to get around this issue.  
I do not have to put them in separate functions.  
![image](https://github.com/user-attachments/assets/fe930f8e-e60e-4dd1-be7e-8ebe12e3c7a6)  
Running `python test_calculator.py` again, it gave this output:  
![image](https://github.com/user-attachments/assets/6cf2e5f9-8de2-4a1a-844a-912a23bdfe9b)  
This is a successful workaround however it takes up many lines of code, much more compared to pytest.
