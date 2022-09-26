class DegreePlot:

    def graph_degree_plot(self, metric):
        #degree    
        dev_x = []
        #number of nodes with such degree
        dev_y = []

        index = 0
            #iterate through each (node,degree) tuple from metric
        for tuple in metric:
            #skip first entry
            if(tuple[0] == 0):
                continue
            elif(tuple[0] == 1):
                dev_x.append(tuple[1])
                dev_y.append(1)
                continue
            #check if the degree is in x axis
            if tuple[1] in dev_x:
                #increment corresponding y index
                index = dev_x.index(tuple[1])
                dev_y[index] = dev_y[index] + 1
            #create new index for x and y axis    
            else:
                #insert degree in x in ascending order, and create an index for corresponding y as well

                for i in reversed(dev_x):
                    check = False
                    if tuple[1] > i:
                        index = dev_x.index(i)    
                        dev_x.insert(index+ 1,tuple[1])
                        dev_y.insert(index +1, 1)
                        check = True
                        break
                #if check is never switched to true, tuple is smaller than everything so insert at beginning
                if check == False:
                    dev_x.insert(0,tuple[1])
                    dev_y.insert(0, 1)
                
        #print(dev_x , "dev_x")
        #print(dev_y , "dev_y")

        # plot graph ------------->
        # x = plt.plot(devX, devY)
        # plt.xlabel('degree')
        # plt.ylabel('# of nodes')
        # plt.title('distribution of nodes degree')
        # plt.show()
        return dev_x,dev_y

        
    #deg = [(0,0), (1,4), (2,4), (3,3),(4,2),(5,5),(6,7),(7,6),(8,1),(9,7),(10,6) ]