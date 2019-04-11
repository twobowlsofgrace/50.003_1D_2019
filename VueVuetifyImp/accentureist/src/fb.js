import firebase from 'firebase/app'
import 'firebase/firestore'

// Initialize Firebase
var config = {
    apiKey: "AIzaSyC3zuNKiAiRhVY2WKCC53NhN3iVojgso-Q",
    authDomain: "accentureist.firebaseapp.com",
    databaseURL: "https://accentureist.firebaseio.com",
    projectId: "accentureist",
    storageBucket: "accentureist.appspot.com",
    messagingSenderId: "237214725796"
  };
  firebase.initializeApp(config); //pass front end to back end

  //need to initiliae and have a starting point for fire store

  const db = firebase.firestore();

  //db.settings({timestampsInSnapshots: true}) //this will result in a warning message
  //need to export the database

  export default db;