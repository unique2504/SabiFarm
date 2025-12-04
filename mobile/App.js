import React, { useState } from 'react';
import { View, Text, Button, Image, StyleSheet, ScrollView } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

export default function App() {
  const [image, setImage] = useState(null);
  const [diseaseResult, setDiseaseResult] = useState('');

  // Pick an image from gallery
  const pickImage = async () => {
    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      quality: 1,
    });

    if (!result.cancelled) {
      setImage(result.uri);
      detectDisease(result.uri);
    }
  };

  // Dummy disease detection function
  const detectDisease = (uri) => {
    // TODO: Replace with real ML model inference
    setDiseaseResult('Healthy (Demo Model)');
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>🌾 FarmSabi Mobile App</Text>

      <Button title="Pick Leaf Image" onPress={pickImage} />

      {image && <Image source={{ uri: image }} style={styles.image} />}

      {diseaseResult ? (
        <Text style={styles.result}>Disease Detection Result: {diseaseResult}</Text>
      ) : null}

      <View style={styles.infoBox}>
        <Text style={styles.infoTitle}>Weather Info:</Text>
        <Text>Temperature: 28°C</Text>
        <Text>Rainfall: 5mm</Text>
        <Text>Humidity: 75%</Text>
      </View>

      <View style={styles.infoBox}>
        <Text style={styles.infoTitle}>Fertilizer Recommendation:</Text>
        <Text>N: 50kg/ha, P: 30kg/ha, K: 20kg/ha</Text>
      </View>

      <View style={styles.infoBox}>
        <Text style={styles.infoTitle}>Planting & Harvest Dates:</Text>
        <Text>Best Planting Date: 10 Dec 2025</Text>
        <Text>Expected Harvest: 20 Mar 2026</Text>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    padding: 20,
    alignItems: 'center',
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    color: '#330033',
    fontWeight: 'bold',
  },
  image: {
    width: 250,
    height: 250,
    marginVertical: 20,
    borderRadius: 10,
  },
  result: {
    fontSize: 18,
    fontWeight: '600',
    marginBottom: 20,
  },
  infoBox: {
    width: '100%',
    padding: 15,
    marginVertical: 10,
    backgroundColor: '#f2f2f2',
    borderRadius: 8,
  },
  infoTitle: {
    fontWeight: 'bold',
    marginBottom: 5,
  },
});
