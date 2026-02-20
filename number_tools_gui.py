import tkinter as tk
from tkinter import messagebox


def reverse_number(n):
    """Reverses the digits of a number"""
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


def is_palindrome(n):
    """Checks if a number is a palindrome"""
    return n == reverse_number(n)


class NumberToolsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Tools")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Title
        title = tk.Label(root, text="Number Tools", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Enter a number:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.input_field = tk.Entry(input_frame, width=15, font=("Arial", 10))
        self.input_field.pack(side=tk.LEFT, padx=5)
        self.input_field.bind("<Return>", lambda e: self.process())
        
        # Buttons frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Process", command=self.process, bg="#4CAF50", fg="white", font=("Arial", 10), padx=20).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear", command=self.clear_all, bg="#f44336", fg="white", font=("Arial", 10), padx=20).pack(side=tk.LEFT, padx=5)
        
        # Results frame
        results_frame = tk.Frame(root, relief=tk.SUNKEN, borderwidth=2, bg="#f0f0f0")
        results_frame.pack(pady=10, padx=15, fill=tk.BOTH, expand=True)
        
        self.result_label = tk.Label(results_frame, text="Results will appear here", font=("Arial", 10), bg="#f0f0f0", justify=tk.LEFT)
        self.result_label.pack(pady=15, padx=15, anchor="w")
    
    def process(self):
        """Process the input number"""
        try:
            num = int(self.input_field.get())
            if num < 0:
                messagebox.showerror("Error", "Please enter a positive integer or zero")
                return
            
            reversed_num = reverse_number(num)
            palindrome = is_palindrome(num)
            
            result_text = f"Original Number: {num}\nReversed Number: {reversed_num}\nIs Palindrome: {'Yes ✓' if palindrome else 'No ✗'}"
            self.result_label.config(text=result_text)
        
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")
            self.input_field.focus()
    
    def clear_all(self):
        """Clear input and results"""
        self.input_field.delete(0, tk.END)
        self.result_label.config(text="Results will appear here")
        self.input_field.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberToolsApp(root)
    root.mainloop()
