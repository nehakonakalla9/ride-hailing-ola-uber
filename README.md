# 🚖 Ride Hailing System (Uber/Ola LLD)

This project is a **Low-Level Design (LLD)** implementation of a ride-hailing platform similar to Uber or Ola.  
It models the core entities, their relationships, and workflows involved in connecting **riders** with **drivers** and managing the complete **trip lifecycle**.

---

## 📌 Features Modeled
- Rider and Driver registration and management
- Ride request and matching to available drivers
- Trip lifecycle: request → allocation → ongoing → completion
- Pricing strategies (default, rating-based, time-based, etc.)
- Extensible strategy design for driver matching and pricing
- Trip metadata handling and management

---

## 🏗️ Class Design

### **1. Core Entities**
- **Rider**
  - Represents a customer.
  - Can request trips, view trip details, and make payments.
- **Driver**
  - Represents a service provider.
  - Has availability status, vehicle details, and can accept/decline rides.
- **Trip**
  - Represents a ride between a rider and driver.
  - Stores status, pricing, and metadata.

---

### **2. Managers**
- **RiderManager**
  - Handles creation, storage, and retrieval of riders.
- **DriverManager**
  - Manages driver onboarding, availability, and lookup.
- **TripManager**
  - Handles creation, allocation, tracking, and completion of trips.
- **StrategyManager**
  - Keeps track of different pricing and driver-matching strategies.

---

### **3. Strategies (Extensible via Strategy Pattern)**
- **Driver Matching Strategies**
  - *Default / Least Time Based*: Assigns driver with minimal wait time.
- **Pricing Strategies**
  - *DefaultPricingStrategy*: Basic fare calculation.
  - *RatingBasedPricingStrategy*: Adjusts fare based on driver rating.
  - *LeastTimeBasedPricingStrategy*: Adjusts fare based on estimated trip time.

---

## 🔗 Class Relationships
- **Rider** requests a **Trip** via **RiderManager**.  
- **TripManager** assigns a **Driver** based on **DriverMatchingStrategy**.  
- **PricingStrategy** determines the fare for the **Trip**.  
- **StrategyManager** allows the system to plug in different strategies at runtime.  
- **TripMetaData** stores additional details about the trip (timestamps, locations, status).  

---

## ⚙️ Example Workflow
1. Rider requests a trip.  
2. `TripManager` consults the active `DriverMatchingStrategy` to select a driver.  
3. A `Trip` is created and assigned.  
4. `PricingStrategy` calculates fare.  
5. Trip lifecycle is updated (requested → allocated → ongoing → completed).  

---

## 📂 Project Structure
