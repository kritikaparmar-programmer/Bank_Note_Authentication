import pickle
import streamlit as st


pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


def home():
    return "Hello"


def predict(variance,skewness,curtosis,entropy):
    """Let's Authenticate the Banks Note 

    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

    
def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance")
    skewness = st.text_input("Skewness")
    curtosis = st.text_input("Curtosis")
    entropy = st.text_input("Entropy")
    result=""
    if st.button("Predict"):
        result=predict(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()