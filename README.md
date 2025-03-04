# Unit-Tests
Unit testing practice, going from simple programs to more complex ones.  
This README is a 'journal' which I am using to help me learn about unit testing.  
There are multiple branches for different sections
## Double
With the function double, which simply doubles a given number, I am testing both if the function works perfectly and if the function does not work perfectly.
This way, I can see how the errors given from the test can help me debug the and discover the problem.
### Testing with pytest
#### Testing without addition error
The function correctly doubles a number.  
Here is what I am testing:  
![image](https://github.com/user-attachments/assets/86f6b9a1-dcee-4c38-9141-97d513fb5b8c)  
Running `pytest test_calculator.py`, it gave this output:  
![image](https://github.com/user-attachments/assets/bd6c1e0a-b821-4705-88fe-ab3c88ac5980)  
Meaning that all tests passed. 
#### Testing with addition error
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
#### Inputting strings
If the user inputs a string, that will happen in the `main` function of `calculator.py`, which I am not testing at the moment. Therefore, I will move the error to occur in the `double` function since I am testing that section. I am achieving this by removing the `int` from the user input and seeing if an error will take place if the user enters a string.
`calculator.py`:  
![image](https://github.com/user-attachments/assets/26f25d89-fedd-4497-a81d-55bd61ca224c)  
Here is my test:  
![image](https://github.com/user-attachments/assets/ef90942e-e6ef-4016-89f3-6074f5550996)  
As shown, no error is raised, but clearly there is a logic error as the program is returning the string twice.
It should return an actual error, therefore I will slightly change the `double` function to this:  
![image](https://github.com/user-attachments/assets/03dd3209-84b6-4433-9050-134b35b1d8c6)  
Testing it, it gives:  
![image](https://github.com/user-attachments/assets/944a2de2-4fcd-4b6d-9943-f48d433f0a6d)  
To include this in `test_calculator.py`, I will raise a ValueError:  
![image](https://github.com/user-attachments/assets/21105a10-f313-4ba3-ae62-773fa1888f96)  
So now it tests strings. Running `pytest test_calculator.py` gives:  
![image](https://github.com/user-attachments/assets/8d17a0bd-1fff-4182-9fe6-8b79df265936)  
