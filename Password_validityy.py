#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 14:12:51 2023

@author: me
"""

def check_password_validity(password):
    # We are going to use flags as checkboxes to remmeber
    #the criterias needed for a valid passowrd , currently they 
    #are set to false because we assume any password doesnt meet 
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False
    
    # Check length of the password 
    if len(password) < 6 or len(password) > 12:
        print("Invalid password length. Length should be between 6 and 12 characters.")
        return
    
    # Check each character in the password
    # if any character checked meets any of the criterias we reverse it from false to true
    
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in ['$','#','@']:
            has_special = True
    
    # Check if all criteria are met else prompt questions 
    if has_lowercase and has_uppercase and has_digit and has_special:
        print("Password is valid.")
    else:
        # Print which criteria are not met
        if not has_lowercase:
            print("Password must contain at least one lowercase letter.")
        if not has_uppercase:
            print("Password must contain at least one uppercase letter.")
        if not has_digit:
            print("Password must contain at least one digit.")
        if not has_special:
            print("Password must contain at least one special character ($, #, or @).")

# Test the function
password = input("Enter a password: ")
check_password_validity(password)
