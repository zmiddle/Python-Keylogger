# Python-Keylogger
## Warning: This program is for academic use only. Do not use this program for malicious purposes.
This is a simple Python keylogger that utilizes the time and pynput libraries.

![Screen shot](https://github.com/zmiddle/Python-Keylogger/blob/main/Keylogger_input.png)
![Screen shot](https://github.com/zmiddle/Python-Keylogger/blob/main/Keylogger_log.png)

### What I learned
* When opening a file to append or write to it has different behaviors. For example if the log.txt didn't exist then you would want to use the "w" (write) arguement to create the file first, then append afterwards. 
* Pynput is a nifty library for recording keys, but I might want to limit the dependencies in future versions.

### Going forward
* I plan on adding a network transfer component to this program (possibly encrypted too) that will transfer the log.txt file to an other destination.

* I need to improve the readability of the log.txt output since having the "'" characters printed after every key press is not ideal and takes up space in the log.txt.

* Some efficiencies with error handling and runtime improvements are also on this list. Maybe I will try and remove the Pynput library for a "live of the land" situation.
