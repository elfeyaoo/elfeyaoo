# PeacefulPlaces — Vacation Rental Website

> A full-stack vacation rental platform, inspired by Airbnb, connecting travelers with hosts for listing, browsing, and booking accommodations.

---

## 📌 Overview

Finding the right vacation rental is time-consuming — travelers struggle to filter listings by budget, location, and amenities, while hosts struggle to manage bookings and availability. **PeacefulPlaces** solves this with a full-stack web platform where hosts can list properties and travelers can search, view details, book, and review stays — all in one place.

---

## ❗ Problem This Solves

- Travelers face a time-consuming, overwhelming search process when filtering properties by budget, location, and amenities
- Hosts struggle to efficiently manage bookings, pricing, and availability
- Inconsistent listing information and poor UX often lead to cancellations or missed bookings
- No single streamlined platform for search, booking, reviews, and location context together

## 🎯 Objectives

- Let users sort/filter vacation rentals based on reviews and ratings
- Provide simple, secure registration and booking flows
- Integrate interactive maps so users can see property locations and nearby context
- Enable hosts to list new properties and manage their listings
- Allow travelers to rate and review stays after booking

---

## 🛠️ Technology Stack

**Frontend:**
- HTML5, CSS3
- Bootstrap 5
- EJS (Embedded JavaScript templates) for dynamic page rendering

**Backend:**
- Node.js
- Express.js

**Database:**
- MongoDB — Collections: Users, Properties, Bookings, Reviews

**Third-Party Integration:**
- MapBox API — interactive maps showing property locations

---

## ⚙️ How It Works

1. **Registration & Login** — Users sign up or log in; credentials are authenticated against MongoDB-stored records.
2. **Browse Listings** — After login, users view all available properties with price, location, and rating shown per listing.
3. **View Property Details** — Selecting a property shows images, description, price, location, and existing reviews.
4. **Book a Property** — Users pick dates and confirm a booking through the booking module.
5. **Rate & Review** — After a stay, users can leave a star rating and written review, visible to future visitors.
6. **Map View** — Each property's location is plotted using the MapBox API so users can see it in geographic context (e.g., relative to Thane, Mumbai, Navi Mumbai).
7. **Add New Listing** — Hosts can create a new listing by submitting a title, description, image link, price, country, and location.

---

## 🏗️ System Architecture

<img width="1081" height="502" alt="image" src="https://github.com/user-attachments/assets/d1a3b657-e36e-4295-a426-6eadc1125ea9" />


---

## 📸 Screenshots

<!-- Paste each screenshot below its heading -->

### Sign Up Page
<img width="1068" height="372" alt="image" src="https://github.com/user-attachments/assets/59567477-5a7c-437a-be1a-18d2fda434c3" />


### Login Page
<img width="1084" height="504" alt="image" src="https://github.com/user-attachments/assets/58d84427-ac16-408e-89e7-47b530b24c0c" />


### All Listings Page
<img width="1083" height="515" alt="image" src="https://github.com/user-attachments/assets/a3c8beb8-eab8-4661-869c-906d5167d496" />


### Property Detail Page
<img width="1087" height="472" alt="image" src="https://github.com/user-attachments/assets/8fad1252-d0f3-4962-8831-a89d705dd181" />


### Add New Listing Page
<img width="1086" height="515" alt="image" src="https://github.com/user-attachments/assets/4dff856e-b578-4f93-aa64-04e6b5f7fb2d" />


### Ratings & Reviews
<img width="1096" height="513" alt="image" src="https://github.com/user-attachments/assets/83ffa217-2770-4478-9722-3b7240c657bb" />


### Map Integration (MapBox)
<img width="1092" height="521" alt="image" src="https://github.com/user-attachments/assets/92215f71-d09d-4ba0-b01e-c4e056765c8b" />


---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/elfeyaoo/My-Projects.git
cd My-Projects/PeacefulPlaces

# Install dependencies
npm install

# Set up environment variables
# MONGO_URI=your_mongodb_connection_string
# MAPBOX_TOKEN=your_mapbox_api_key

# Run the application
npm start
```

## ⚠️ Known Gaps / Honest Notes for Future Work

A few things worth being upfront about (both for your own future development and if asked about this project in an interview):

- **No trained ML model is actually implemented.** The "recommendation" feature currently works by sorting listings on reviews/ratings — it's not a collaborative-filtering or content-based ML model yet, despite early planning documents mentioning one. If you want this resume-worthy as a Data Science project, this is the single highest-impact addition: even a basic collaborative filtering model (e.g., using `scikit-surprise` or a simple weighted rating + similarity approach) would make the "AI-powered" framing accurate.
- **No chatbot/NLP assistant is implemented** — this was an early objective but isn't present in the current build.
- **No payment gateway is actually integrated yet** — bookings are recorded, but real transaction processing isn't live.

---

## 🔮 Future Scope

- Implement an actual recommendation engine (collaborative filtering or content-based) using booking/review data
- Add the planned NLP-powered chatbot for real-time query handling
- Integrate a real payment gateway (e.g., Razorpay/Stripe) for live transactions
- Add dynamic pricing based on demand, seasonality, and reviews
- Expand to travel-service integrations (flights, car rentals) for a full trip-planning experience
- Add booking-conflict handling (locking mechanism) to prevent double bookings at scale

---

## 📄 License

*(Add a license if you intend for others to reuse this code — MIT is a common choice for student/portfolio projects.)*
