import pandas as pd
import randomuser 

# pip install randomuser
def get_some_data():
    users=[]
    for user in randomuser.RandomUser.generate_users(20):
        users.append({
        'Name':user.get_full_name(),
        'Gender':user.get_gender(),
        "City":user.get_city(),
        "State":user.get_state(),
        "Email":user.get_email(), 
        "DOB":user.get_dob(),
        "Picture":user.get_picture()
    })
    return pd.DataFrame(users)

get_some_data()
df1 = pd.DataFrame(get_some_data())
print(df1) 