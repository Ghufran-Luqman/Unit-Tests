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
