// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional


const firebaseConfig = {
        apiKey: process.env.REACT_APP_FIREBASEAPIKEY,
        authDomain: process.env.REACT_APP_AUTHDOMAINFIREBASE,
        projectId: process.env.REACT_APP_FIREBASE_PROJECTID
};
      
      // Initialize Firebase
export const firebaseApp = initializeApp(firebaseConfig);



