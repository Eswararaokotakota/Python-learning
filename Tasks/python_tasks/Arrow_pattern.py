              #
                #
                  #
                    #
                      #
                        #
                          #
# # # # # # # # # # # # # # # 
                          #
                        #
                      #
                    #
                  #
                #
              #         
while True:
  step = int(input("Enter an even number:")) 
  if step%2 != 0 :
    print("\U0001F622","The entered number is not even, Please try another number")
    continue  
  else:           
    # step = 5  
              
    n = step+1 # iterations

    objects = int(step/2)
    space ="   "
    for i in range(n):
        if i >= objects:
            if i==objects:
                for k in range(objects*3):
                    print("#", end=space)
                print("")
            else:
                for l in range(1,step+1):
                    if l == step:
                        print("#")
                    else:
                        print(space, end=" ")   
            print("")
            step-=1
            continue
        else:
            for j in range(1,step+1):
                if j == step:
                    print("#")
                else:
                    print(space, end=" ")

        step+=1
        if step == (step*2)-2:
            break
        print("")
  print("We did it!","\U0001F60E")
  break