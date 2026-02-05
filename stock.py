#TASK 3: Stock Portfolio Tracker
#● Goal: Build a simple stock tracker that calculates total investment based on manually defined stockprices.
#● Simplified Scope:
#○ User inputs stock names and quantity.
#○ Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}).
#○ Display total investment value and optionally save the result in a .txt or .csv file.
#● Key Concepts Used: dictionary, input/output, basic arithmetic, file handling(optional).

if __name__=="__main__":  # runs on direct calling of program
       d={"AAPL":180,"TSLA":250}   #dictionary stores stock and price
       stock=input("Enter the stock name : ") #getting stock name
       quantity=int(input("Enter the quantity : ")) #getting the number of stock 
       investment=quantity*d[stock]
       print("Total investment for stock ",stock," of quantity ",quantity," is ",investment)
       #printting statment which covers all stock name, quantity and investment

       #optional
       f=open("invest.txt","a") # need of the file creation and mode of a-append
       f.write(stock+"-"+str(quantity)+"-"+str(investment)+"\n") 
       f.close()    #getting stored the investment details in the file