# Unit-Tests
Unit testing practice, going from simple programs to more complex ones.  
This README is a 'journal' which I am using to help me learn about unit testing.
## Double
With the function double, which simply doubles a given number, I am testing both if the function works perfectly and if the function does not work perfectly.
This way, I can see how the errors given from the test can help me debug the and discover the problem.
### Testing without pytest
#### Testing without errors
The function correctly doubles a number. 
Running `test_calculator.py` gave me nothing meaning that no errors occurred.
#### Testing with error
The error is that the double function adds 2 to the given number rather than multiplying it by 2.
Running `test_calculator.py`, it gave this error:

![image](https://github.com/user-attachments/assets/b6f36d54-e2e8-4c97-9681-dd0aa415c1c5)

This means that the test failed at the `assert double(3) == 6`, meaning that when 3 is currently passed into this version of double, the output is not 6.  
However, the test was successful at `assert double(2) == 4`. This is a coincidence since 2*2=4 and 2+2=4.  
Therefore, this prompts me to look at my double function and see that it has a logical error, allowing me to fix it.  
The tests give me clues on what the error could be (if there is one) so therefore it must be more efficient to use all types of tests (such as valid, invalid, boundary, erroneous) rather than only multiple tests of one type as it will allow me to narrow down the error quicker, saving time.

### Testing with pytest
#### Testing without errors
The function correctly doubles a number.  
Here is what I am testing:  
![image](https://github.com/user-attachments/assets/86f6b9a1-dcee-4c38-9141-97d513fb5b8c)  
Running `pytest test_calculator.py`, it gave this output:  
![image](https://github.com/user-attachments/assets/bd6c1e0a-b821-4705-88fe-ab3c88ac5980)  
Meaning that all tests passed. 

#### Testing with errors
The error is that the double function adds 2 to the given number rather than multiplying it by 2.  
I am testing 2, 3, and 0 as above.  
Running `pytest test_calculator.py`, it gave this output:  
![image](https://github.com/user-attachments/assets/0d68cc31-fc90-4979-93a8-b27ab5d86490)  
This means the test failed at 3, it did not try 0.  
pytest gives a hint as to what it is trying to equate, as shown it is trying to equate 5 and 6, and it shows the function where 5 came from.  
This way, I can easily narrow down the function causing this error, and perhaps debug that function further using breakpoints for example to exactly pinpoint the error if it was a larger, more complex function.  

#### Multiple tests
By default, pytest will stop at the first failed test. To get around this issue, I can simply put the other tests into new functions. This way, I can have more clues as to what is going wrong in my function.  
![image](https://github.com/user-attachments/assets/90790bc6-939d-4015-9f3b-ee5f7186815d)  
##### Without error
Now, if I run `pytest test_calculator.py` when `double` is working correctly, I get:  
![image](https://github.com/user-attachments/assets/e6ff47e9-7ef4-456f-ac62-410f5da917db)  
Showing that all three passed (the dots give a very fast way to tell which ones pass and fail).

##### With error
If I run `pytest test_calculator.py` when `double` adds 2 instead of multiplying by 2, I get:
![image](https://github.com/user-attachments/assets/d50934b4-a0ff-4434-b3f4-41b28a609813)  
This shows the details of all the tests, allowing me to further pinpoint errors, which is again more useful for more complex functions.
