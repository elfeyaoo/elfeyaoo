# PeacefulPlaces — Vacation Rental Website

> A full-stack vacation rental platform, inspired by Airbnb, connecting travelers with hosts for listing, browsing, and booking accommodations.

---

## 📌 Overview

Finding the right vacation rental is time-consuming — travelers struggle to filter listings by budget, location, and amenities, while hosts struggle to manage bookings and availability. **PeacefulPlaces** solves this with a full-stack web platform where hosts can list properties and travelers can search, view details, book, and review stays — all in one place.

**Team:** Mini Project — Third Year Engineering, CSE (Data Science)
- Sharayu Mahajan (22107051)
- Kalpana Mohanty (22107059)
- Rishi Mane (22107063)
- Avadhoot Virkar (22107064)

**Project Guide:** Mr. Vaibhav Yavalkar
**Institute:** A.P. Shah Institute of Technology, University of Mumbai (Academic Year 2024–25)

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

<!-- Paste your system architecture / use case / DFD diagrams below -->



---

## 📸 Screenshots

<!-- Paste each screenshot below its heading -->

### Sign Up Page


### Login Page


### All Listings Page


### Property Detail Page


### Add New Listing Page


### Ratings & Reviews


### Map Integration (MapBox)


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
*(Adjust these commands to match your actual project structure and entry file, e.g. `node app.js` or `nodemon index.js`.)*

---

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

## 👥 Team

- **Avadhoot Virkar** — [GitHub](https://github.com/elfeyaoo)
- **Sharayu Mahajan**
- **Kalpana Mohanty**
- **Rishi Mane**

*Project Guide: Mr. Vaibhav Yavalkar*

---

## 📄 License

*(Add a license if you intend for others to reuse this code — MIT is a common choice for student/portfolio projects.)*
