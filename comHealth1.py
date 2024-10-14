from tkinter import *
import customtkinter
from PIL import Image
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green 




root = customtkinter.CTk()

#name , size and logo
root.title('comHealth')
root.iconbitmap('images/comhelath logo.jpeg')
root.geometry("500x400")

# heading for the main frame
header=customtkinter.CTkLabel(root, text="Welcome to comHealth , please try our ML powered tools ",font = ("Arial", 15, "bold"))
header.pack(pady = 5)

#image for the main frame
my_image = customtkinter.CTkImage(light_image=Image.open('images/comhelath logo.jpeg'), dark_image=Image.open('images/comhelath logo.jpeg'), size=(250,180))
my_label= customtkinter.CTkLabel(root , text="" , image= my_image)
my_label.pack(pady=20)


#window for the diabetes predictor
def diabetes_predict():
    new_window1=customtkinter.CTkToplevel(root)
    new_window1.title("Predict your chances of diabetes")
    new_window1.geometry("950x500")

    #heading for the insurance cost predictor
    header2=customtkinter.CTkLabel(new_window1,text="Tell us a few things about yourself to predict your chances of diabetes", font = ("Arial", 15, "bold"))
    header2.pack(pady = 5)

    #image for the insurance cost predictor
    my_image2 = customtkinter.CTkImage(light_image=Image.open('images/blood sugar monitor.jpeg'), dark_image=Image.open('images/blood sugar monitor.jpeg'), size=(250,180))
    my_label2= customtkinter.CTkLabel(new_window1, text="" , image= my_image2)
    my_label2.pack(pady=20)


    #custom frame to input data
    frame2= Frame(new_window1, background="#3b3b3b")
    frame2.pack()

    preg_label=customtkinter.CTkLabel(master=frame2, text="No of pregnancies :",font = ("Arial", 15, "bold"))
    preg_label.grid(row=1,column =1 , padx=10,pady=5)

    preg_entry=customtkinter.CTkEntry(master=frame2)
    preg_entry.grid(row=1,column=2,padx=10,pady=5)

    gluc_label=customtkinter.CTkLabel(master=frame2, text="Blood glucose :",font = ("Arial", 15, "bold"))
    gluc_label.grid(row=1,column =3 , padx=10,pady=5)

    gluc_entry=customtkinter.CTkEntry(master=frame2)
    gluc_entry.grid(row=1,column=4,padx=10,pady=5)

    bp_label=customtkinter.CTkLabel(master=frame2, text="Blood pressure :",font = ("Arial", 15, "bold"))
    bp_label.grid(row=2,column =1 , padx=10,pady=5)
    
    bp_entry=customtkinter.CTkEntry(master=frame2)
    bp_entry.grid(row=2,column=2,padx=10,pady=5)

    st_label=customtkinter.CTkLabel(master=frame2, text="Skin thickness :",font = ("Arial", 15, "bold"))
    st_label.grid(row=2,column =3 , padx=10,pady=5)

    st_entry=customtkinter.CTkEntry(master=frame2)
    st_entry.grid(row=2,column=4,padx=10,pady=5)

    insu_label=customtkinter.CTkLabel(master=frame2, text="Insulin :",font = ("Arial", 15, "bold"))
    insu_label.grid(row=3,column =1 , padx=10,pady=5)

    insu_entry=customtkinter.CTkEntry(master=frame2)
    insu_entry.grid(row=3,column=2,padx=10,pady=5)

    bmi_label=customtkinter.CTkLabel(master=frame2, text="BMI :",font = ("Arial", 15, "bold"))
    bmi_label.grid(row=3,column =3 , padx=10,pady=5)

    bmi_entry=customtkinter.CTkEntry(master=frame2)
    bmi_entry.grid(row=3,column=4,padx=10,pady=5)

    dp_label=customtkinter.CTkLabel(master=frame2, text="Diabetes pedigree fn:",font = ("Arial", 15, "bold"))
    dp_label.grid(row=4,column =1 , padx=10,pady=5)

    dp_entry=customtkinter.CTkEntry(master=frame2)
    dp_entry.grid(row=4,column=2,padx=10,pady=5)

    age_label=customtkinter.CTkLabel(master=frame2, text="AGE :",font = ("Arial", 15, "bold"))
    age_label.grid(row=4,column =3 , padx=10,pady=5)

    age_entry=customtkinter.CTkEntry(master=frame2)
    age_entry.grid(row=4,column=4,padx=10,pady=5)

    predict_label=customtkinter.CTkLabel(new_window1, text="", font=("Arial", 15 , "bold" ))
    predict_label.pack(pady=5)

    def predict_diab():
        modeldiab=pickle.load(open('models/diabetes.pkl','rb'))
        entry1=float(preg_entry.get())
        entry2=float(gluc_entry.get())
        entry3=float(bp_entry.get())
        entry4=float(st_entry.get())
        entry5=float(insu_entry.get())
        entry6=float(bmi_entry.get())
        entry7=float(dp_entry.get())
        entry8=float(age_entry.get())

        
        input_data = (entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8)

        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        scaler= StandardScaler()
        scaler.fit(input_data_reshaped)
        # standardize the input data
        std_data = scaler.transform(input_data_reshaped)

        prediction = modeldiab.predict(std_data)

        if (prediction[0] == 0):
            predict_label.configure(text="the person is non diabetic")
        else:
            predict_label.configure(text="the person is diabetic")


    button_diab= customtkinter.CTkButton(master=new_window1, text="Predict", command = predict_diab)
    button_diab.pack(pady=5)


   




#window for insurance predictor
def insurance_pred():
    new_window2=customtkinter.CTkToplevel(root)
    new_window2.title("Predict your possible health insurance costs")
    new_window2.geometry("900x500")

    #heading for the insurance cost predictor
    header2=customtkinter.CTkLabel(new_window2,text="Tell us a few things about yourself to predict the cost of your health insurance", font = ("Arial", 15, "bold"))
    header2.pack(pady = 5)

    #image for the insurance cost predictor
    my_image3 = customtkinter.CTkImage(light_image=Image.open('images/insurance predict.jpeg'), dark_image=Image.open('images/insurance predict.jpeg'), size=(250,180))
    my_label3= customtkinter.CTkLabel(new_window2, text="" , image= my_image3)
    my_label3.pack(pady=20)

    #custom frame to input data
    frame3= Frame(new_window2, background="#3b3b3b")
    frame3.pack()

    #age column
    age_label=customtkinter.CTkLabel(master=frame3, text="Enter age :",font = ("Arial", 15, "bold"))
    age_label.grid(row=1,column =1 , padx=10,pady=5)

    age_entry=customtkinter.CTkEntry(master=frame3)
    age_entry.grid(row=1,column=2,padx=10,pady=5)

    #sex column
    sex_label=customtkinter.CTkLabel(master=frame3, text="Enter gender male(0)/female(1) :",font = ("Arial", 15, "bold"))
    sex_label.grid(row=1,column =3 , padx=10,pady=5)

    sex_entry=customtkinter.CTkEntry(master=frame3)
    sex_entry.grid(row=1,column=4,padx=10,pady=5)

    #bmi column
    bmi_label=customtkinter.CTkLabel(master=frame3, text="Enter bmi :",font = ("Arial", 15, "bold"))
    bmi_label.grid(row=2,column =1 , padx=10,pady=5)

    bmi_entry=customtkinter.CTkEntry(master=frame3)
    bmi_entry.grid(row=2,column=2,padx=10,pady=5)

    #children column
    child_label=customtkinter.CTkLabel(master=frame3, text="Enter the no of children :",font = ("Arial", 15, "bold"))
    child_label.grid(row=2,column =3 , padx=10,pady=5)

    child_entry=customtkinter.CTkEntry(master=frame3)
    child_entry.grid(row=2,column=4,padx=10,pady=5)

    #smoker column
    smoker_label=customtkinter.CTkLabel(master=frame3, text="smoker yes(0)/no(1) :",font = ("Arial", 15, "bold"))
    smoker_label.grid(row=3,column =1 , padx=10,pady=5)

    smoker_entry=customtkinter.CTkEntry(master=frame3)
    smoker_entry.grid(row=3,column=2,padx=10,pady=5)

    #region column
    region_label=customtkinter.CTkLabel(master=frame3, text="Enter region SE(0)/SW(1)/NE(2)/NW(3) :",font = ("Arial", 15, "bold"))
    region_label.grid(row=3,column =3 , padx=10,pady=5)

    region_entry=customtkinter.CTkEntry(master=frame3)
    region_entry.grid(row=3,column=4,padx=10,pady=5)

    predict_label=customtkinter.CTkLabel(new_window2, text="", font=("Arial", 10 , "bold" ))
    predict_label.pack(pady=10)

    def predict_ins():
        modelinsu=pickle.load(open('models/insurance.pkl','rb'))
        entry1=float(age_entry.get())
        entry2=float(sex_entry.get())
        entry3=float(bmi_entry.get())
        entry4=float(child_entry.get())
        entry5=float(smoker_entry.get())
        entry6=float(region_entry.get())

        input_data = (entry1,entry2,entry3,entry4,entry5,entry6)

        # changing input_data to a numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = modelinsu.predict(input_data_reshaped)

        predict_label.configure(text="Your insurance cost is : "+str(prediction[0]), font = ("Arial",15,"bold"))
        

    button_ins= customtkinter.CTkButton(master=new_window2, text="Predict", command = predict_ins)
    button_ins.pack(pady=15)





 
#new custom frame to place the buttons
frame1 = Frame(root, background="#3b3b3b")
frame1.pack()

button1= customtkinter.CTkButton(master=frame1, text="Insurance cost >", command = insurance_pred)
button1.grid(row=5,column = 2, padx = 10, pady=5)

button2 = customtkinter.CTkButton(master=frame1, text="Diabetes predictor >", command=diabetes_predict)
button2.grid(row=5 , column =5, padx= 10, pady=5)



root.mainloop()