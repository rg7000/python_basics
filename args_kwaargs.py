def print_msg(msg, error="No error", *args, **kwargs):
    print("Log: "+error+"\t"+msg)
    print("Args", args)
    print("kwargs", kwargs)
print_msg("This will be logged", "File not found", 13, 14, 15, "Key1", "Key2")
