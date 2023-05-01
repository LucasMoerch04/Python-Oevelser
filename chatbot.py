import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as CTk

root = CTk.CTk()
root.geometry("1000x780")
CTk.set_appearance_mode("light")


entry = CTk.CTkEntry(root,width=320,height=80) 
entry.place(x=10,y=640)

text = tk.StringVar()

user_input="\n"



def button_event():
    user_input=entry.get()
    text.set(current_text + user_text + user_input)
    
    if user_input == "reset":
        text.set(bot_text + welcome_text)
    #TOPIC 1 - Locations
    elif user_input == "1":
        
        text.set(user_text + user_input + bot_text + location)
    
    elif user_input == "1a":
        text.set(user_text + user_input + bot_text + hq)
    
    elif user_input == "1b":
        text.set(user_text + user_input + bot_text + visit)
       
    
    #TOPIC 2 - Focus areas
    elif user_input == "2":
        text.set(user_text + user_input + bot_text + focus_areas)
    elif user_input == "2a":
        text.set(user_text + user_input + bot_text + a2)
    elif user_input == "2b":
        text.set(user_text + user_input + bot_text + b2)
    elif user_input == "2c":
        text.set(user_text + user_input + bot_text + c2)
    elif user_input == "2d":
        text.set(user_text + user_input + bot_text + d2)
    elif user_input == "2e":
        text.set(user_text + user_input + bot_text + e2)
    elif user_input == "2f":
        text.set(user_text + user_input + bot_text + f2)
    elif user_input == "2g":
        text.set(user_text + user_input + bot_text + g2)
    elif user_input == "2h":
        text.set(user_text + user_input + bot_text + h2)
        
    #TOPIC 3 - Contact Us
    elif user_input == "3":
        text.set(user_text + user_input + bot_text + contact)


label = CTk.CTkLabel(root,textvariable =text,width=980,height=600, bg_color="white",anchor=NW,justify=LEFT,font=("Times New Roman", 18))
label.place(x=10,y=10)
    
button = CTk.CTkButton(root,text="Enter",command=button_event,height=80, width=30)
button.place(x= 340,y=640)


bot_text =( """\nDOLLbot: """)

user_text= """\nYou: """

#Welcome text from DOLLbot
welcome_text = """Hi. I am DOLL Living Labs chatbot. I am here to give you answers to the most frequently asked questions about us.
                  
                  You can provide inputs by typing your wished topic code (e.g. 1 or 2b).
                  To come back to the beginning, simply type "reset".
                  
                  Choose one of these topics:
                  1. Location
                  2. Focus Areas
                  3. Contact us
                  \n\n"""


text.set(bot_text + welcome_text)

current_text = bot_text + welcome_text


#Location - FAQs
location = """Choose:
              1a. Where is your headquarters located?  
              1b. Visitation. 
              """


#Location - a - Answer
hq = """DOLL Living Labs' headquarters is located in Albertslund, 
Danmark, at the adress: Liljens Kvarter 2. DOLL also have a Visitor 
Center located in Glostrup, Danmark, at the adress: Naverland 2.
"""
#Location - b - Answer
visit = """We welcome groups and delegations to visit DOLL Living Lab 
in-person. You can meet our partners, and experience DOLL as a co-creation 
platform around new city technology.
At DOLL we can offer guided tours, partner presentations, sparring sessions 
and workshops where we involve subject-matter experts, industry players and 
other key partners to make your visit informative and inspirational."""


#Focus Areas - FAQs
focus_areas = """DOLL Living Lab a unique platform where you can find the 
                latest Smart City technologies, intelligent traffic systems, 
                and outdoor lighting solutions. We bring public and private 
                actors together on a neutral ground, where we can test, 
                showcase, and be inspired by cutting edge technology in a 
                “one stop shop” with all relevant network infrastructures 
                present across our 400 acre living lab.
                
            Choose a focus area below to learn more:
              2a. Dynamic lighting
              2b. Enviromental monitoring
              2c. Intelligent lighting
              2d. Intelligent traffic system
              2e. Network
              2f. Smart Pole
              2g. Smart waste
              2h. System and dataplatform
              """

#Focus Area - Answers - a
a2 = """
        Dynamic lighting is one of the areas that DOLL Living Labs is investing in 
        and has been inventing solutions for.
        Dynamic lighting refers to the ability to adjust the intensity, color, and 
        distribution of light in a given space based on different parameters such 
        as time of day, occupancy, and task requirements. This technology can provide 
        numerous benefits, including energy savings, improved well-being, and increased 
        productivity.

        One of the key innovations that DOLL Living Labs has developed for dynamic 
        lighting is the use of sensors and data analytics to optimize lighting levels 
        in real-time. This involves installing a network of sensors that detect the 
        presence of occupants and the amount of natural light in a room. The data 
        collected is then analyzed and used to adjust the intensity and color of 
        artificial lighting to create the optimal lighting conditions for a particular 
        space.

        Another area of focus for DOLL Living Labs is the use of circadian lighting 
        to promote human health and well-being. Circadian lighting is a type of dynamic 
        lighting that mimics the natural cycle of daylight, with warm and cool light tones 
        that change throughout the day. Research has shown that exposure to circadian lighting 
        can help regulate our sleep-wake cycles and improve mood, alertness, and cognitive performance.

        DOLL Living Labs has also been exploring the use of dynamic lighting for outdoor 
        environments, such as public spaces and roads. By adjusting the intensity and color of 
        streetlights based on the time of day and the level of activity in a given area, it is 
        possible to create a more inviting and safe environment for pedestrians and cyclists.
"""

#Focus Area - Answers - b
b2 = """DOLL livings labs are at the forefront of creating innovative solutions for environmental 
        monitoring. The labs are dedicated to researching and developing smart technologies that 
        can help improve the environment and protect it from further degradation.

        One of the significant inventions from the DOLL livings labs is the development of advanced 
        sensors that can monitor the air quality. These sensors can measure the levels of pollutants 
        in the air, such as carbon monoxide, nitrogen oxide, and particulate matter. With this data, 
        environmentalists can make informed decisions to improve the quality of the air in the region.

        The livings labs are also developing sophisticated systems that can detect water contamination 
        in the environment. These systems use advanced technologies to analyze the water quality and 
        detect any potential contaminants. The information from these systems can help to prevent water 
        pollution and protect the health of the local community.

        Another major invention from the DOLL livings labs is the development of smart grids that can 
        monitor energy consumption. These systems use advanced algorithms and machine learning to analyze 
        energy usage patterns and suggest ways to reduce energy consumption. By reducing energy usage, we 
        can reduce carbon emissions and slow down the effects of climate change.

        DOLL livings labs are continually pushing the boundaries of innovation in environmental monitoring. 
        With their cutting-edge technologies and solutions, we are helping to create a more sustainable 
        world for future generations.
        """

#Focus Area - Answers - c        
c2 = """DOLL living labs are leading the way in developing intelligent lighting systems. These systems 
        combine advanced sensors, controls, and network technologies to create energy-efficient, adaptive 
        lighting solutions for homes, businesses, and public spaces. Here are some of the innovations that 
        DOLL living labs are inventing in the field of intelligent lighting:

        1) Adaptive lighting: DOLL living labs are developing lighting systems that can adapt to changing conditions. 
        This means that the lighting will adjust its brightness and color temperature based on factors such as 
        occupancy, time of day, and ambient light levels. By doing so, the lighting system can optimize energy 
        use while providing the right level of illumination for the task at hand.

        2) Networked lighting: DOLL living labs are creating lighting systems that can be controlled and monitored 
        remotely through a network. This allows users to adjust the lighting in real-time, track energy usage, 
        and identify maintenance needs. By integrating lighting with other building systems, such as HVAC and 
        security, DOLL living labs are creating smart, connected buildings that are more efficient and comfortable.

        3) Human-centric lighting: DOLL living labs are researching how lighting can affect human health and 
        well-being. We are designing lighting systems that can adjust the color temperature and intensity of 
        light to align with our circadian rhythms. This can have a positive impact on our sleep patterns, mood, 
        and productivity.

        4) Sustainable lighting: DOLL living labs are developing lighting systems that are energy-efficient and 
        sustainable. We are incorporating renewable energy sources, such as solar and wind, to power the lighting. 
        we are also using energy-efficient LED bulbs and fixtures to reduce energy consumption and maintenance costs.

        """


#Focus Area - Answers - d
d2 = """DOLL livings labs are at the forefront of inventing innovative solutions for intelligent traffic systems. 
        Intelligent traffic systems are becoming increasingly important as urban areas grow and the number of vehicles 
        on the road increases. The goal of intelligent traffic systems is to make traffic flow more smoothly, reduce 
        congestion, and enhance safety for drivers, passengers, and pedestrians.

        DOLL livings labs are working on a range of solutions for intelligent traffic systems. One of their main areas 
        of focus is developing advanced traffic management systems that use real-time data to optimize traffic flow. 
        These systems can help to reduce congestion by directing traffic to less congested routes and by dynamically 
        adjusting traffic signals to respond to changing traffic patterns.

        Another area of focus for DOLL livings labs is developing intelligent transportation systems that can help to 
        reduce the number of accidents on the road. These systems use advanced sensors, cameras, and machine learning 
        algorithms to detect potential hazards on the road and warn drivers before an accident occurs.

        DOLL livings labs are also developing innovative solutions for improving public transportation. One example is 
        the development of advanced bus rapid transit (BRT) systems that use dedicated lanes to move buses quickly and 
        efficiently through urban areas. These BRT systems can help to reduce congestion, improve air quality, and 
        provide more efficient transportation options for commuters.
    
    """

#Focus Area - Answers - e
e2 = """DOLL Living Labs is a leading innovation hub that specializes in developing and testing advanced technologies 
        for the transportation industry. As part of their work in the Network focus area, DOLL Living Labs is currently 
        inventing a multi-modal traffic sensor with visual edge AI.

        This innovative technology is designed to provide real-time insights into traffic conditions, helping cities 
        and transportation agencies to optimize their traffic management strategies. The multi-modal traffic sensor is 
        capable of detecting various types of vehicles, including bicycles, cars, and trucks, and can also detect 
        pedestrians and other objects in the roadway.

        The visual edge AI technology used in the sensor is capable of analyzing the video data captured by the sensor 
        to identify traffic patterns and predict traffic flow. This information can be used to adjust traffic signals, 
        reroute traffic, and optimize traffic flow in real-time.

        One of the key benefits of this technology is its ability to improve safety on the roads. By detecting and 
        analyzing traffic patterns, transportation agencies can identify potential hazards and take steps to reduce 
        the risk of accidents.
    """

#Focus Area - Answers - f
f2 = """One of the main goals of this focus area is to improve street lighting, which is traditionally a costly and 
        energy-intensive process. To achieve this, DOLL Living Labs is developing smart lighting systems that are 
        capable of adapting to different lighting conditions and adjusting their brightness accordingly. This means 
        that streetlights will only use the necessary amount of energy, reducing costs and improving energy efficiency.

        Another area of focus is the integration of various smart sensors and technologies on the poles. These could 
        include traffic sensors, air quality monitors, and cameras. By placing these technologies on the poles, the city 
        can collect data and monitor the city's activity, ultimately enabling decision-makers to improve urban planning 
        and make informed decisions for the city's growth.

        DOLL Living Labs is also developing communication systems that can be integrated with the smart poles. This will 
        enable the public to access Wi-Fi and other communication services while on the go, and also provide a platform 
        for emergency alerts and other notifications.

    """

#Focus Area - Answers - g
g2 = """One of the key inventions that DOLL Living Labs is working on is the development of smart waste bins. These bins 
        are equipped with sensors that can detect when the bin is full and send an alert to waste management companies, 
        enabling them to schedule pickups more efficiently. The sensors can also detect the type of waste being disposed 
        of and provide insights into the volume and composition of waste generated by a particular area.

        In addition to smart waste bins, DOLL Living Labs is also working on developing smart waste sorting systems. 
        These systems use advanced algorithms to sort waste into different categories such as recyclables, organic waste, 
        and non-recyclables. The system can also detect hazardous waste and separate it for safe disposal.

        Another invention being developed by DOLL Living Labs is a mobile waste compactor. This device can compress waste 
        to reduce its volume, making it easier to transport and dispose of. The device is equipped with sensors that can 
        detect the level of compression and send alerts when the waste needs to be emptied.

        DOLL Living Labs is also developing a waste-to-energy system that can convert organic waste into biogas, which can 
        be used as a source of renewable energy. The system can help reduce greenhouse gas emissions and provide a sustainable 
        solution for waste management.

        In conclusion, DOLL Living Labs is making significant strides in the Smart Waste focus area by developing innovative 
        solutions that can improve waste management and promote sustainability. These inventions have the potential to 
        revolutionize the waste management industry and contribute to a cleaner and more sustainable future.
    """

#Focus Area - Answers - h
h2 = """DOLL Living Labs are at the forefront of innovative solutions for the System and Dataplatform focus area. We are 
        inventing technologies that transform the way we interact with data, and providing new opportunities for businesses 
        to make informed decisions.

        One of the key areas of focus for DOLL Living Labs is the development of advanced data management systems. We are 
        working to create smart systems that can collect and process data in real-time, providing businesses with critical 
        insights that can help them optimize their operations and drive growth.

        In addition, DOLL Living Labs are also exploring the potential of machine learning and AI technologies in the context 
        of data management. By developing sophisticated algorithms and models, we are enabling businesses to analyze vast 
        amounts of data with greater accuracy and efficiency, allowing them to make more informed decisions and stay ahead 
        of the competition.

        Another area of focus for DOLL Living Labs is the development of new tools and technologies for data visualization. 
        By creating intuitive and interactive dashboards, we are making it easier for businesses to understand and explore 
        their data, and to quickly identify areas for improvement and optimization.
"""

#Contact us - FAQ's
contact = """Please don't hesitate to contact us if you're interested in visiting DOLL Living Lab, have any questions or would 
            like to explore a partnership opportunity. We also encourage inquiries from students who are interested in 
            community digitization.
            
            You can contact members of our team with the information below or on our LinkedIn profile:
            
            LinkedIn: https://www.linkedin.com/company/doll-living-lab/
            
            Teddy Sibbern Axelsen - Head of DOLL Living Labs        Frederik Bøllingtoft - Student Assistant at DOLL Living Labs
            Mail:   teddy.sibbern.axelsen@webuilddenmark.dk           Mail:   frederik.bollingtoft@webuilddenmark.dk
            Phone:  +45 23837079                                                    Phone:  +45 24441264
            
            Clara Røder - Project Manager at DOLL Living Labs         Jacob Kriegbaum Caspersen - Technology Lead at DOLL Living Labs
            * Currently on Maternity Leave                                        Mail:   jacob.kriegbaum.caspersen@webuilddenmark.dk
                                                                                                  Phone:  +45 24248951
             
            Ben Cahill - Innovation at DOLL Living Labs
            Mail:   ben.cahill@webuilddenmark.dk
            Phone:  +45 21173066
            
            Hedvig Spang-Hanssen - Visitor Services Coordinator at DOLL Living Labs
            Mail:   doll@webuilddenmark.dk
            Phone:  +45 53547003
            
            Helle Bygholm - Communications Consultant at DOLL Living Labs
            Mail:   helle.bygholm@gate21.dk
            Phone:  +45 53847003
"""

root.mainloop()