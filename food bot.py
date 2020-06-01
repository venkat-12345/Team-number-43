menu={
    "veg-manchuria":{"name":"Veg-Manchuria","price":40,"code":"xa"},
    "chicken-manchuria":{"name":"Chiken-Manchuria","price":60,"code":"xb"},
    "veg-friedrice": {"name":"Veg-Friedrice","price":40,"code":"xc"},
    "chicken-friedrice":{"name":"Chicken-Friedrice","price":50,"code":"xd"}
    }
reflections={
    "xa":"veg-manchuria",
    "xb":"chicken-manchuria",
    "xc":"veg-friedrice",
    "xd":"chicken-friedrice",
    "veg-manchuria":"veg-manchuria",
    "chicken-manchuria":"chicken-manchuria",
    "veg-friedrice":"veg-friedrice",
    "chicken-friedrice":"chicken-friedrice"
     }
numbers={
        "a":1,
        "1":1,
        "one":1,
        "2":2,
        "two":2,
        "3":3,
        "three":3,
        "4":4,
        "four":4,
        "5":5,
        "five":5,
        "6":6,
        "six":6,
        "7":7,
        "seven":7,
        "8":8,
        "eight":8,
        "9":9,
        "nine":9,
        "10":10,
        "ten":10
  }
help_rules=[
    "help","help!","help me","what","what?"
    ]
order_rules=[
    "get me a","get me the","get me","get","I would like to have","would like to" 
    ]
removal_rules=[
    "remove","cancel","nevermind"
    ]
query_rules=[
    "price of","cost of","how much"
    ]
bill_rules=[
    "my order","my bill"
    ]
order=dict()
def print_menu():
    for dish,info in menu.items():
        print("~~"+info["name"]+"-"+"₹"+str(info["price"])+"--"+info["code"])
def print_order():
    total=0
    for dish,num in order.items():
        
        print("~~"+menu[reflections[dish]]['name']+" Quantity "+str(num))
        total+=menu[reflections[dish]]['price']*num
    print("Your total is",total)
def respond(message):
    output="I did'nt get\n try help to get info"
    message=message.lower()
    for rule in order_rules:
        if rule in message:
            message=message[message.find(rule)+len(rule):]
            message=message.strip().split(" ")
            k=1
            for i in message:
                if i in numbers:
                    k=numbers[message.pop(message.index(i))]
            for i in message:
                if reflections[i] in menu:
                    order[i]=k
                    output="Yes added to your order"
    for rule in removal_rules:
        if rule in message:
            message=message[message.find(rule)+len(rule):]
            message=message.strip().split(" ")
            for i in message:
                if reflections[i] in menu:
                    k=order.pop(i)
                    output="Yes done"
    for rule in query_rules:
        if rule in message:
            message=message[message.find(rule)+len(rule):]
            message=message.strip().split(" ")
            for i in message:
                if reflections[i] in menu:
                    i=reflections[i]
                    output= menu[i]["name"]+"is ₹"+str(menu[i]["price"])
    for rule in bill_rules:
        if rule in message:
            if order:
                print_order()
                output="Is there any thing else I can do"
            else:
                output="You haven't odderd anything yet"
    for rule in help_rules:
        if rule in message:
            output='Guys I am here to help you make me help you\nTry using the target words\nTo order food:  Try words; get.get me,i would like to have\tNote: Please order one item at an instance\nTo get the info : Try words; price of ,cost of ,how much\nTo remove : Try words; remove,never mind,cancel\nTo get the bill: Try words ; my order ,my bill'


    return output
def send_message():
    print("User:",end="")
    message=input()
    k=respond(message)
    print("\nBot:"+k)
print("Hi this is H.A.V.S \nI am named after the first letters of my creators \nI can help you with odering your food\nHere is the menu (try using get a xa)")
print_menu()
while(True):
    send_message()
