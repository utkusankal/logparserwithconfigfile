#!/usr/bin/env python
# coding: utf-8

# In[59]:


import LogParser_config as log


# In[60]:


def log_parser(filename):
    parsed_results=[]
    
    result1=[]
    
    
    
    with open(filename, 'r') as logfile:
        
        
        for line in logfile:   
            log_type=line[22:26]
            key_list=[]
            
            if log_type in log.keys_ranges.keys():
                result=[]
                
                for key in log.keys_ranges[log_type]:
                    
                    key_list.append(key)
                    for value in log.keys_ranges[log_type][key]:
                        
                        
                        start_ind=log.keys_ranges[log_type][key][0]
                        end_ind=log.keys_ranges[log_type][key][1]
                    #print(line[start_ind:end_ind])
                    data=line[start_ind:end_ind]
                      
                    result.append((data))
                
                
                result1=[]
                
                for i in result:
                        try:
                            k=i.strip()
                            
                            result1.append(k)
                            
                        except:
                            pass
                res=dict(zip(key_list,result1))
                
                res["DynamicValues"]=res["DynamicValues"].split(" ")
                #print(res["DynamicValues"])
                templist=res["DynamicValues"]
                templist[:] = [item for item in templist if item != '']
                        
                res["DynamicValues"]=templist
                final_res=[]
                final_res.append(res)
                    
                
                f = open('%s.txt' % log_type, 'a')
                    #result=map(lambda x:x+'\n', result)
                
                f.write(str(final_res)+"\n")
                    
                f.close()
                    
                
                  
                    
                
              
                    
                    
            


# In[61]:


log_parser("tca.log")


# In[ ]:




