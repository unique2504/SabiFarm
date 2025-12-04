import React, { useState } from "react";
import { View, Text, Button, Image, StyleSheet, ScrollView, TextInput } from "react-native";
import * as ImagePicker from "expo-image-picker";

export default function App() {
  const [image, setImage] = useState(null);
  const [disease, setDisease] = useState("");
  const [fertilizer, setFertilizer] = useState({});
  const [weather, setWeather] = useState({});
  const [calendar, setCalendar] = useState({});
  const [market, setMarket] = useState({});
  const [cropType, setCropType] = useState("Maize");

  const backendUrl = "http://YOUR_BACKEND_URL"; // Replace with actual FastAPI URL

  const pickImage = async () => {
    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      quality: 1
    });
    if (!result.cancelled) {
      setImage(result.uri);
      uploadImage(result);
    }
  };

  const uploadImage = async (img) => {
    const formData = new FormData();
    formData.append("file", {
      uri: img,
      name: "leaf.jpg",
      type: "image/jpeg"
    });

    const res = await fetch(`${backendUrl}/disease`, {
      method: "POST",
      body: formData,
      headers: {
        "Content-Type": "multipart/form-data"
      }
    });
    const data = await res.json();
    setDisease(data.disease);
    fetchOtherFeatures();
  };

  const fetchOtherFeatures = async () => {
    const fertRes = await fetch(`${backendUrl}/fertilizer?crop_type=${cropType}&land_fertility=70`);
    setFertilizer(await fertRes.json());

    const weatherRes = await fetch(`${backendUrl}/weather?location=Lagos`);
    setWeather(await weatherRes.json());

    const calRes = await fetch(`${backendUrl}/crop_calendar?crop_type=${cropType}`);
    setCalendar(await calRes.json());

    const marketRes = await fetch(`${backendUrl}/market?crop_type=${cropType}&expected_yield_kg=100`);
    setMarket(await marketRes.json());
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>🌾 FarmSabi Mobile App</Text>

      <Text>Crop Type:</Text>
      <TextInput style={styles.input} value={cropType} onChangeText={setCropType} />

      <Button title="Pick Leaf Image" onPress={pickImage} />

      {image && <Image source={{ uri: image }} style={styles.image} />}

      {disease ? <Text>Disease: {disease}</Text> : null}

      {fertilizer.N && (
        <View style={styles.box}>
          <Text>Fertilizer Recommendation:</Text>
          <Text>N: {fertilizer.N} P: {fertilizer.P} K: {fertilizer.K}</Text>
          <Text>{fertilizer.notes}</Text>
        </View>
      )}

      {weather.temperature && (
        <View style={styles.box}>
          <Text>Weather in Lagos:</Text>
          <Text>Temp: {weather.temperature}°C, Humidity: {weather.humidity}%, Rainfall: {weather.rainfall}mm</Text>
        </View>
      )}

      {calendar.best_planting_date && (
        <View style={styles.box}>
          <Text>Crop Calendar:</Text>
          <Text>Planting: {calendar.best_planting_date}</Text>
          <Text>Harvest: {calendar.expected_harvest_date}</Text>
        </View>
      )}

      {market.current_price && (
        <View style={styles.box}>
          <Text>Market Report:</Text>
          <Text>Price: {market.current_price} NGN/kg, Expected Revenue: {market.expected_revenue} NGN</Text>
        </View>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flexGrow: 1, padding: 20, backgroundColor: "#fff", alignItems: "center" },
  title: { fontSize: 24, fontWeight: "bold", color: "#330033", marginBottom: 20 },
  image: { width: 250, height: 250, marginVertical: 20, borderRadius: 10 },
  box: { width: "100%", padding: 10, marginVertical: 10, backgroundColor: "#f2f2f2", borderRadius: 8 },
  input: { borderWidth: 1, borderColor: "#ccc", padding: 5, width: "100%", marginBottom: 10, borderRadius: 5 }
});
