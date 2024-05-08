from importlib.metadata import files
import pandas as pd # type: ignore
import numpy as np # type: ignore
import statistics
import streamlit as st # type: ignore
st.write("Hello Streamlit! this is my first app.")
st.title("Waste Generation")
st.subheader("Group 2")
st.write("The client at KORU IMPACT SOLUTIONS is working on a project to automate impact reports for fund managers investing in sustainable stocks.")
st.write("Waste in itself has a diﬀerent nature of origin, negative impact, ways of its further utilisation. Some kinds of it can be used further in order to achieve other goals and needs that are not related to their generation, others can no longer be used for human beneﬁts taking into account existing achievements.")
st.write("Here are some insights of my findings along with some recommendations.")
st.title("Waste Management Insights and Recommendations on General Analysis")
st.write("A general analysis with the primary waste, secondary waste, and total waste could get us some information and trends in waste management for European countries for a period of 10 years.")
st.write("Overall, primary waste, originating from sources like households and industries, dominates total waste generation, evidenced by its higher average and maximum values compared to secondary waste. Although secondary waste contributes to the overall waste stream, it's generated in smaller quantities or as a by-product of primary waste treatment. The positive correlation between primary and total waste implies the relationship between primary and total waste indicates that eﬀorts to manage primary waste eﬀectively could have a signiﬁcant impact on reducing overall waste generation.")
st.title("Waste Management Insights and Recommendations on the Environment")
st.write("For environmental analysis, I used soil contamination, water pollution and deforestation each contributing signiﬁcantly to environmental damage. For soil contamination, Germany, France and the UK have signiﬁcantly higher values than the rest with France being the most. All these countries have massive industrial practices that damage the soil threw equipment and harmful chemicals. For water pollution, it follows the same trend this makes sense due to the process of leaching. Leaching is a process where rainwater washes away harmful chemicals oﬀ the soil into the water leading to water contamination/pollution. Finally, for deforestation, we see a diﬀerent trend where Germany is actually the lead in terms of deforestation. Also, Finland showing a signiﬁcant increase along with Sweden and multiple other countries.")
st.write("Deforestation has the highest correlation with the other waste categories almost a perfect correlation. This suggests that deforestation practices almost certainly lead to water pollution and soil contamination. So addressing deforestation issues as No.1 priority is a must.Some ways to prevent deforestation: Urbanisation: consider building more flats or in other words making buildings small but long this will still make room for people without taking up considerable amounts of land. Planting greenery on top of each building is also a solid option that many countries are already incorporating. Natural disasters: Wildfires can be reduced by investing in firefighting resources and better monitoring and early detection practices. Illegal logging: By enforcing harsher penalties or deploying law enforcers that protect the trees. Some ways to reduce soil contamination and water pollution is by: Chemicals: Try using less harmful chemicals and when used store and dispose of them safely.")
st.title("Waste Management Insights and Recommendations on Health")
st.write("For the health analysis, I used Food waste, Household waste, Plastic waste, Chemical waste and tried to ﬁnd some interesting insights. Which categories are standing out in waste production for one or more reasons. Food waste in Italy and the United Kingdom is standing out followed by Germany because of population and industrial people. In household waste, Turkey and the United Kingdom are the highest and followed by Germany and France. In plastic waste, Italy is on the top, and then Germany followed by the United Kingdom because of awareness. In chemical waste, the United Kingdom is on the top and then France has more chemical waste then others. To cut down on waste, focus on reducing consumption, reusing items, and recycling materials. Educate the public on waste reduction and proper disposal methods. Encourage composting of organic waste and separate recyclables from regular trash. Advocate for reduced packaging and implement regulations to limit waste. Invest in innovative solutions and collaborate with stakeholders for effective waste management.")
st.title("Waste Management Insights and Recommendations on Society")
st.write("For Society analysis, I used soil, public health and discarded vehicles each contributing signiﬁcantly to Society. Soil: If the soil quality is poor in the country with the highest value, this can have several impacts on society: Bad soil can lead to environmental issues like erosion and loss of biodiversity. The economy can suﬀer if agriculture is a big part of it and the soil quality is low, leading to higher food prices and imports. Improving soil quality is important for the health and wealth of a country's society and environment. I found out that for discarded vehicles,France has the highest value.France is a country that has a high population When a country has a lot of discarded vehicles, it can lead to pollution and take up space that could be used for something else. If there are a lot of people in that country, these problems can get worse because there are more cars to get rid of, and the pollution can affect more people. It's important for countries to find good ways to deal with old cars so they don't harm the environment or people's health.")
st.title("Waste Management Insights and Recommendations on Carbon Intensity")
st.write("For the Carbon Intensity, i choose Waste Incineration, Disposal of Plastic waste and Landfill. And tried to study some interesting insights. Which countries produce more waste in different categories. For Disposal of Plastic i found that the UK and Germany are the main countries in this category, followed by Spain and France, this can lead to the production of toxic gases. In the Landfill waste, Germany and Turkey are leading in this category for one of the countries that produce landfill waste, followed by Netherlands which in the last years has increase the waste in Landfill. This has several consequences like it can release toxins and create leachate that pollutes land, ground, and water. Landfill also releases the greenhouse gas methane. These problems with landfill can all have negative effects on the local environment and the health of people and wildlife who live in the nearby area. For Waste Incineration, i found that the leading countries are Estonia and Germany, this can lead to creates and/or releases harmful chemicals and pollutants, including: Air pollutants such as particulate matter, which cause lung and heart diseases. So, the recommendations i made, are to implement a waste minimisation programme, reuse and recycle materials in house. Redesign processes to reduce or eliminate waste production, and finally implementing gas cleaning systems that helps to remove pollut from emissions, reducing air pollution and utilising waste to generate electricity or heat buildings maximises efficiency.")


#Feedback form
def main():
    st.title('Feedback Form')

    # Add feedback questions
    st.write('Please provide your feedback:')
    app_feedback = st.text_area('How did you find the app?')
    app_usefulness = st.radio('Was it useful?', options=['Yes', 'No'])
    app_recommendation = st.radio('Would you recommend it to someone in the future?', options=['Yes', 'No'])

    # Submit feedback
    if st.button('Submit Feedback'):
        # Save feedback to file or database
        save_feedback(app_feedback, app_usefulness, app_recommendation)
        st.write('Thank you for your feedback!')

def save_feedback(feedback, usefulness, recommendation):
    # Write feedback to file or database
    # For demonstration, we'll just print the feedback
    print('Feedback:', feedback)
    print('Usefulness:', usefulness)
    print('Recommendation:', recommendation)

if __name__ == '__main__':
    main()
