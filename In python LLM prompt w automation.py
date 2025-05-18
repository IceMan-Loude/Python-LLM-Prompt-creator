import tkinter as tk

def get_llm_response(prompt):
    return "This is a simulated response."

def submit_prompt():
    prompt = prompt_entry.get()
    if prompt.strip():
        conversation.config(state='normal')
        conversation.insert(tk.END, "User: " + prompt + "\n")
        response = get_llm_response(prompt)
        conversation.insert(tk.END, "LLM: " + response + "\n")
        conversation.config(state='disabled')
        conversation.see(tk.END)
        prompt_entry.delete(0, tk.END)

root = tk.Tk()
root.title("LLM Interaction")
root.geometry("600x400")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=0, column=1, sticky='ns')

conversation = tk.Text(root, state='disabled', yscrollcommand=scrollbar.set)
conversation.grid(row=0, column=0, sticky='nsew')
scrollbar.config(command=conversation.yview)

prompt_entry = tk.Entry(root)
prompt_entry.grid(row=1, column=0, sticky='ew')
prompt_entry.bind('<Return>', lambda event: submit_prompt())

submit_button = tk.Button(root, text="Submit", command=submit_prompt)
submit_button.grid(row=1, column=1)

prompt_entry.focus_set()

root.mainloop()