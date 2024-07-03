# autoregister

### This program automatically register hundreds of products into a web-based system using Selenium driver + Pandas + Python

## Initial Problem

The program is based on the open project from Hashtag Training based on PyAutoGUI. However, the original project had several limitations I wanted to overcame:
1. It was not portable: it depends totally on local coordinates of each machine, so it could be plug and play
2. It was not within best practices: PyAutoGUI is not robust for Web Scraping and Web Automation projects

## Solution

I redesign the entire code to be deployed with Selenium webdriver, a much better choice for this kind of project. It is fast, reliable and easy to command each step.

There are 4 steps in the solution:

### 1. Open the system web page
### 2. Login into the system
### 3. Import product database using Pandas
### 4. Register all the products with a loop
