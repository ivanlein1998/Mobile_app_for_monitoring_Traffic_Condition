import React from "react";
import { StyleSheet, Text, View, Image} from "react-native";
import MapView, { Callout, Marker, PROVIDER_GOOGLE } from 'react-native-maps'; // remove PROVIDER_GOOGLE import if not using Google Maps=
import * as firebase from 'firebase';
import {Svg, Image as ImageSvg} from 'react-native-svg';

var carCount = [0,0,0,0,0,0]


const styles = StyleSheet.create({
 container: {
   height: '100%',
   width: '100%',
   justifyContent: 'flex-end',
   alignItems: 'center'
 },
 map: {
    height: '100%',
    width: '100%'
 },
 text:{
  flex: 0,
   height: 400,
   width: 700,
  alignItems: 'flex-start'
 },
 image:{
  flex: 10,
  height: 400,
  width: 400,
  alignSelf: 'flex-start'
 },
});

const firebaseConfig = {
  apiKey: "AIzaSyAnB7odOZ1fJzpMbiy3krQPR3ZqlOS9_UY",
  authDomain: "fypdb-ivanleinnn.firebaseapp.com",
  projectId: "fypdb-ivanleinnn",
  storageBucket: "fypdb-ivanleinnn.appspot.com",
  messagingSenderId: "79093803907",
  appId: "1:79093803907:web:ae8df8a4ce23e8b644e4b6",
  databaseURL: "https://fypdb-ivanleinnn-default-rtdb.firebaseio.com",
};
// Initialize Firebase

if (firebase.apps.length === 0) {
  firebase.initializeApp(firebaseConfig);
}

const roadImages = [require('./imgs/mcdowell_rd_detected.jpg'),require('./imgs/90th_st_detected.jpg'),
require('./imgs/camelback_rd_detected.jpg'),
require('./imgs/glendale_ave_detected.jpg'),
require('./imgs/northern_ave_detected.jpg'),
require('./imgs/via_de_ventura_detected.jpg'),]

const images = [require('./icon/0.png'),require('./icon/1.png'),
require('./icon/2.png'),
require('./icon/3.png'),
require('./icon/4.png'),
require('./icon/5.png'),
require('./icon/6.png'),
require('./icon/7.png'),
require('./icon/8.png'),
require('./icon/9.png'),
require('./icon/10.png'),
require('./icon/11.png'),
require('./icon/12.png'),
require('./icon/13.png'),
require('./icon/14.png'),
require('./icon/15.png'),
require('./icon/16.png'),
require('./icon/17.png'),
require('./icon/18.png'),
require('./icon/19.png'),
require('./icon/20.png'),
require('./icon/21.png'),
require('./icon/22.png'),
require('./icon/23.png'),
require('./icon/24.png'),
require('./icon/25.png'),
require('./icon/26.png'),
require('./icon/27.png'),
require('./icon/28.png'),
require('./icon/29.png'),
require('./icon/30.png')]

firebase.database().ref('/fyp_data/mcdowell_rd_num_of_car').on('value',(snap)=>{
carCount[0] = snap.val();
});


firebase.database().ref('/fyp_data/90th_st_num_of_car').on('value',(snap)=>{
carCount[1] = snap.val();
});

firebase.database().ref('/fyp_data/camelback_rd_num_of_car').on('value',(snap)=>{
carCount[2] = snap.val();
});

firebase.database().ref('/fyp_data/glendale_ave_num_of_car').on('value',(snap)=>{
carCount[3] = snap.val();
});

firebase.database().ref('/fyp_data/northern_ave_num_of_car').on('value',(snap)=>{
carCount[4] = snap.val();
});

firebase.database().ref('/fyp_data/via_de_ventura_num_of_car').on('value',(snap)=>{
carCount[5] = snap.val();

});


export default class google_map extends React.Component{
  render(){
    return(
      <View style={styles.container}>
        <MapView
          provider={PROVIDER_GOOGLE} // remove if not using Google Maps
          style={styles.map}
          region={{
            latitude: 33.5,
            longitude: -112.0,
            latitudeDelta: 0.4,
            longitudeDelta: 0.4,
          }}>
          <Marker
            coordinate = {{latitude: 33.464316980770015, longitude: -112.2970453667987}}
            title = {'mcdowell_rd'}>
            <Image style = {{width: 70,height: 70}} source={images[carCount[0]]}  resizeMode = {'contain'} onLoad={() => this.forceUpdate()}></Image>
            <Callout>
              <View style = {{width: 800,height: 800, alignItems:'flex-start'}}  onLoad={() => this.forceUpdate()}>
              <Svg width={900} height={900}>
                 <ImageSvg
                     width={'100%'} 
                     height={'100%'}
                     href={roadImages[0]}
                     onLoad={() => this.forceUpdate()}
                 />
             </Svg>
             <Text>Phoenix, Mcdowell road, Car Count:{carCount[0]}</Text>      
              </View>    
            </Callout>
          </Marker>
          <Marker
            coordinate = {{latitude: 33.61997380149239, longitude: -111.89127517419321}}
            title = {'90th_st'}>
            <Image  style = {{width: 70,height: 70}} source={images[carCount[1]]} resizeMode = {'contain'} onLoad={() => this.forceUpdate()}></Image>
            <Callout>
            <View style = {{width: 900,height: 900, alignItems:'flex-start'}}  onLoad={() => this.forceUpdate()}>
              <Svg width={900} height={900}>
                 <ImageSvg
                     width={'100%'} 
                     height={'100%'}
                     href={roadImages[1]}
                     onLoad={() => this.forceUpdate()}
                 />
             </Svg>                 
              </View>
            </Callout>
          </Marker>
          <Marker
            coordinate = {{latitude: 33.90220961274939, longitude: -111.93901069563307}}
            title = {'camelback_rd'}>
            <Image  style = {{width: 70,height: 70}} source={images[carCount[2]]} resizeMode = {'contain'} onLoad={() => this.forceUpdate()}></Image>
            <Callout>
            <View style = {{width: 900,height: 900, alignItems:'flex-start'}}  onLoad={() => this.forceUpdate()}>
              <Svg width={900} height={900}>
                 <ImageSvg
                     width={'100%'} 
                     height={'100%'}
                     href={roadImages[2]}
                     onLoad={() => this.forceUpdate()}
                 />
             </Svg>
             <Text>Scottsdale, North 90th street, Car Count:{carCount[1]}</Text>  
              </View>
            </Callout>
          </Marker>
          <Marker
            coordinate = {{latitude: 33.538008936928726, longitude: -112.2161421821383}}
            title = {'glendale_ave'}>
            <Image  style = {{width: 70,height: 70}} source={images[carCount[3]]} resizeMode = {'contain'} onLoad={() => this.forceUpdate()}></Image>
            <Callout>
            <View style = {{width: 900,height: 900, alignItems:'flex-start'}} onLoad={() => this.forceUpdate()}>
              <Svg width={900} height={900}>
                 <ImageSvg
                     width={'100%'} 
                     height={'100%'}
                     href={roadImages[3]}
                     onLoad={() => this.forceUpdate()}
                 />
             </Svg> 
             <Text>hoenix, Camelback road, Car Count:{carCount[2]}</Text>   
              </View>
            </Callout>
          </Marker>
          <Marker
            coordinate = {{latitude: 33.55274312777665, longitude: -112.20729846679637}}
            title = {'northern_ave'}>
            <Image  style = {{width: 70,height: 70}} source={images[carCount[4]]} resizeMode = {'contain'}  onLoad={() => this.forceUpdate()}></Image>
            <Callout>
            <View style = {{width: 900,height: 900, alignItems:'flex-start'}} onLoad={() => this.forceUpdate()}>
              <Svg width={900} height={900}>
                 <ImageSvg
                     width={'100%'} 
                     height={'100%'}
                     href={roadImages[4]}
                     onLoad={() => this.forceUpdate()}
                 />
             </Svg>
             <Text>Glendale, Northern Parkway, Car Count:{carCount[4]}</Text>
              </View>
            </Callout>
          </Marker>
          <Marker
            coordinate = {{latitude: 33.55342554514627, longitude: -111.8937726091256}}
            title = {'via_de_ventura'}>
            <Image  style = {{width: 70,height: 70}} source={images[carCount[5]]} resizeMode = {'contain'}  onLoad={() => this.forceUpdate()}></Image>
            <Callout>
            <View style = {{width: 900,height: 900, alignItems:'flex-start'}} onLoad={() => this.forceUpdate()}>
              <Svg width={900} height={900}>
                 <ImageSvg
                     width={'100%'} 
                     height={'100%'}
                     href={roadImages[5]}
                     onLoad={() => this.forceUpdate()}
                 />
             </Svg>
             <Text>Scottsdale, Via de ventura, Car Count:{carCount[5]}</Text>
              </View>
            </Callout>
          </Marker>
        </MapView>
    
  </View>)
  
  }
}