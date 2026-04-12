# fithub
## Table of Contents
## Table of Contents

- [Project Goals](#project-goals)
- [Live Project](#live-project)
- [Screenshot](#screenshot)
- [User Stories](#user-stories)
  - [View Workout Details](#view-workout-details)
  - [Access Premium Workouts](#access-premium-workouts)
  - [Subscribe to Premium Plan](#subscribe-to-premium-plan)
  - [Track Workout Completion](#track-workout-completion)
  - [Login to Account](#login-to-account)
  - [View Fitness Progress](#view-fitness-progress)
  - [Create an Account](#create-an-account)
  - [Contact Site Owner](#contact-site-owner)
  - [About Page](#about-page)
  - [Manage Fitness Profile](#manage-fitness-profile)
  - [Manage Shop Products](#manage-shop-products)
  - [Manage Workouts](#manage-workouts)
  - [Browse Shop Products](#browse-shop-products)
  - [Add Products to Cart](#add-products-to-cart)
  - [Provide Delivery Address](#provide-delivery-address)
  - [View Customer Orders](#view-customer-orders)
- [Database Models and Schema](#database-models-and-schema)
  - [Authentication & User Management](#authentication--user-management-django-allauth)
  - [Shop Models](#shop-models)
  - [Workout Management Models](#workout-management-models)
  - [Payments & Premium](#payments--premium)
  - [Contact & Communication](#contact--communication)
- [Wireframes](#wireframes)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Images](#images)
  - [Icons](#icons)
- [Features](#features)
  - [Home App](#home-app)
  - [Workout App](#workout-app)
  - [Progress Tracking](#progress-tracking)
  - [Authentication System](#authentication-system-django-allauth)
  - [Payments App](#payments-app)
  - [Shop App](#shop-app)
  - [Profile App](#profile-app)
  - [Admin Management](#admin-management)
  - [Pages App](#pages-app)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
  - [Languages](#languages-used)
  - [Django Extensions](#django-and-django-extensions-used)
  - [Frameworks, Libraries & Programs](#frameworks-libraries-and-programs)
- [Deployment](#deployment)
  - [GitHub Setup](#github-setup)
  - [Heroku Deployment](#heroku-deployment)
  - [Amazon AWS Setup](#amazon-aws-setup)
  - [Local Setup](#local-setup)
- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)


 

## Project Goals 
Fithub is a dynamic fitness web application built with Django, PostgreSQL, and modern front-end technologies. It allows users to explore workout plans, track exercise progress, and access premium content through secure authentication and Stripe integration. The platform is designed with a responsive interface and user-friendly experience, supporting profile management, progress tracking, and communication features. The project follows best practices to deliver a scalable, secure, and fully functional fitness platform.     
 
--- 
## Live Project  
- [View the live project here.](https://fit-hub-e72d29259775.herokuapp.com/) 

## Screenshot  
### Home page screenshot. 

 <div align="center">
    <img src="docs/images/home_page.png" alt="image of the homepage">
</div>

 
## User Stories 
 
### View Workouts Details
   
As a visitor, I want to view a detailed workout plan, So that I can understand the exercises included.
 
**Acceptance Criteria** 
- Acceptance criteria 1: Clicking a workout plan opens the full plan page.
 
- Acceptance criteria 2: The page displays:

    -title

    -difficulty level

    -description

    -list of exercises
- Acceptance criteria 3: Premium workouts show a locked message for non-subscribers.
 
### Access Premium Workouts

As a subscribed user, I want to access premium workouts, So that I can benefit from advanced training plans.
 
**Acceptance Criteria** 
- Acceptance criteria 1: Only users with an active subscription can view premium workouts.
- Acceptance criteria 2: Non-subscribed users see a subscription prompt.
- Acceptance criteria 3: Backend verification prevents bypassing access. 
 
### Subscribe to Premium Plan  
As a registered user, I want to purchase a monthly subscription, So that I can access premium workout plans.
 
**Acceptance Criteria** 
- Acceptance criteria 1: Subscription page displays plan details and price.
- Acceptance criteria 2: Users are redirected to Stripe checkout.
- Acceptance criteria 3: Successful payment activates the subscription.
- Acceptance criteria 4: Premium workout plans become accessible.
 
### Track Workout Completion
As a registered user, I want to mark workouts as completed, So that I can track my fitness progress. 
 
**Acceptance Criteria** 
- Acceptance criteria 1: Users can mark workouts as completed.
- Acceptance criteria 2: Completion status is saved in the database.
- Acceptance criteria 3: Progress displays on the user dashboard.
 
### Login to Account 
As a registered user, I want to log into my account, So that I can access my profile, workouts, and purchases.
 
**Acceptance Criteria** 
- Acceptance criteria 1: Login form is accessible.
- Acceptance criteria 2: Correct credentials log the user in.
- Acceptance criteria 3: nvalid credentials show an error message.
- Acceptance criteria 4: User is redirected to their dashboard or homepage.
 
### View Fitness Progress
As a registered user,   
As a registered user, I want to see my workout progress, So that I can monitor my improvement.
 
**Acceptance Criteria** 
- Acceptance criteria 1: Dashboard displays:

    -Completed workouts

    -Total workouts

    -Completion percentage

- Acceptance criteria 2: Progress updates dynamically.

### Create an Account  
As a visitor, I can register for an account, so that I can track my fitness progress and access premium content. 
 
**Acceptance Criteria** 
- Acceptance criteria 1: Registration form is available.
- Acceptance criteria 2: Valid detail create a new user account.
- Acceptance criteria 3: A profile and Subscription record are automatically created.
- Acceptance criteria 4: Users is redirected to the homepage after successful registration.
 
### Contact Site Owner
As a visitor, I want to contact the platform owner, so that I can ask questions or report issues. 
 
**Acceptance Criteria** 
- Acceptance criteria 1: Contact form is accessible.

- Acceptance criteria 2: Form includes:
    - Name
    - Email
    - Message

- Acceptance criteria 3: Form submission sends the message successfully.
 
### About Page   
As a visitor, I want to learn about the platform, So that I understand what services FitHub offers.
 
**Acceptance Criteria** 
- Acceptance criteria 1: About page is accessible from navigation.
- Acceptance criteria 2: Page describes:

    - Platform purpose

    - Services offered

    - Subscription benefits

- Acceptance criteria 3: Page is responsive and readable on all devices.
 
--- 
### Manage Fitness Profile
As a registered user, I want to update my fitness profile, So that I can personalize my experience.

**Acceptance Criteria** 
- Acceptance criteria 1: Users can update:

    -picture

    -bio

- Acceptance criteria 2: Changes are saved to the database.

- Acceptance criteria 3: Profile updates immediately reflect on the profile page.
 

### Manage Shop Products
As an admin, I want to manage digital products, So that I can sell fitness guides and resources.

**Acceptance Criteria** 
- Acceptance criteria 1: Admin can create products.

- Acceptance criteria 2: Admin can edit or remove products.

- Acceptance criteria 3: Products appear automatically in the shop.

### Manage Workouts
As an admin, I want to create, edit, and delete workout plans, So that I can maintain the site’s content.

**Acceptance Criteria** 
- Acceptance criteria 1: Admin can manage workout plans via Django Admin.
- Acceptance criteria 2: Admin can add exercises to workouts.
- Acceptance criteria 3: Changes are reflected immediately on the site.

### Browse Shop Products
As a visitor, I want to browse fitness products, So that I can purchase workout equipment and guides.

**Acceptance Criteria**
- Acceptance criteria 1: Shop page displays all available products
- Acceptance criteria 2: Products show image, name, price, and stock status
- Acceptance criteria 3: Products are displayed in a responsive grid layout
- Acceptance criteria 4: Users can click on products to view details

### Add Products to Cart
As a user, I want to add products to my cart, So that I can purchase multiple items at once.

**Acceptance Criteria**
- Acceptance criteria 1: Products have an "Add to Cart" button
- Acceptance criteria 2: Cart shows quantity and total price
- Acceptance criteria 3: Users can update or remove items from cart
- Acceptance criteria 4: Cart persists in session for non-logged-in users

### Provide Delivery Address
As a customer, I want to enter my delivery address at checkout, 
So that my purchased items can be shipped to me.

**Acceptance Criteria**
- Acceptance criteria 1: Checkout process includes a delivery information form

- Acceptance criteria 2: Form requires full name, email, phone number, and address

- Acceptance criteria 3: Address fields include street, city, postal code, and country

- Acceptance criteria 5: Delivery information is saved before payment is processed

### View Customer Orders
As an admin, I want to see all customer orders, So that I can process and fulfills them.

**Acceptance Criteria**

- Acceptance criteria 1: Admin can view list of all orders with order numbers

- Acceptance criteria 2: Each order shows customer name, total amount, and date

- Acceptance criteria 5: Order details show which products were purchased

### Database Models and Schema

### Models Overview

#### Authentication & User Management (Django Allauth)

**User** (Built-in Django User Model)
- Fields: username, email, password, is_active, is_staff, date_joined, last_login
- Role: Base user authentication and account management
- Relationships: 
  - One-to-One with UserProfile
  - One-to-Many with Orders
  - One-to-Many with Deliveries

**UserProfile** (profiles/models.py)
- Fields: user, bio, profile_image, is_premium
- Purpose: Extends user with fitness profile information and premium status
- Relationships: Belongs to One User
- Special: Auto-created via Django signals when user registers

**Delivery** (profiles/models.py)
- Fields: user, full_name, email, phone_number, address_line1, address_line2, city, postal_code, country, created_at
- Purpose: Stores customer shipping addresses for product deliveries
- Relationships: Belongs to One User (ForeignKey)
- Features: Full address property method for formatted addresses

#### Shop 

**Product** (shop/models.py)
- Fields: name, description, price, image, stock
- Purpose: Manages fitness products available for purchase
- Features: 
  - Stock tracking for inventory management
  - Image upload support via AWS S3
  - Low stock warnings (admin feature)

**Order** (shop/models.py)
- Fields: user, created_at, total, paid
- Purpose: Tracks customer purchase transactions
- Relationships: 
  - Belongs to One User
  - Has many OrderItems
- Features: Paid status tracking for order fulfillment

**OrderItem** (shop/models.py)
- Fields: order, product, quantity, price
- Purpose: Individual line items within an order
- Relationships: 
  - Belongs to One Order
  - Belongs to One Product
- Features: Captures price at time of purchase (historical record)

#### Workout Management

**Workout** (workouts/models.py)
- Fields: title, description, difficulty, duration, is_premium
- Purpose: Fitness workout plans for users
- Features:
  - is_premium flag for premium content restriction
  - Difficulty levels (Beginner, Intermediate, Advanced)
- Relationships: Has many Exercises

**Exercise** (workouts/models.py)
- Fields: workout, name, sets, reps, duration
- Purpose: Individual exercises within workout plans
- Relationships: Belongs to One Workout

**Progress** (workouts/models.py)
- Fields: user, exercise, completed, completed_at
- Purpose: Tracks user workout completion progress
- Relationships:
  - Belongs to One User
  - Belongs to One Exercise
- Features: Timestamp tracking for completion history

#### Payments & Premium

**Stripe Integration**
- Used for secure payment processing
- Handles checkout sessions and transactions
- Ensures safe handling of payment data

**Functionality:**
- Users can purchase premium access
- Payments are processed securely via Stripe
- Payment status is stored in the database
- Checkout session management
- Secure metadata storage (order_id, user_id)

**Premium Access Control**
- Activated automatically after successful Stripe payment
- Admin can manually grant/revoke premium status

#### Contact & Communication

**Contact Form** (pages app)
- Fields: name, email, message
- Purpose: Customer inquiries and support requests
- Features:
  - Email notification to site owner
  - Auto-reply confirmation to customer
  - Gmail SMTP integration

#### Django Allauth (Authentication System)
- **Purpose**: Complete user authentication management
- **Features**:
  - Handles user authentication workflows
  - Email verification and account management
  - Secure login, logout, and registration
  - Password reset functionality
- **Functionality**:
  - Users can register with email confirmation
  - Secure session management
  - Account recovery options

- Database Diagram

  - The database diagram shows a list of items in each object and relationships between each object.

    <div align="center"><img src="readme-images/page_images/QuickDBD-export.png" alt="image of the database diagram"></div>

## WireFrames

  - Phone
    - [Wireframes for phones.](readme-images/wireframes/phone.pdf)
  - Tablet
    - [Wireframes for tablets.](readme-images/wireframes/tablet.pdf)
  - Desktop
    - [Wireframes for desktops.](readme-images/wireframes/desktop.pdf)

## Database models and schema
### Models Overview

#### Authentication & User Management (Django Allauth)

**User** (Built-in Django User Model)
- Fields: username, email, password, is_active, is_staff, date_joined, last_login
- Role: Base user authentication and account management
- Relationships: 
  - One-to-One with UserProfile
  - One-to-Many with Orders
  - One-to-Many with Deliveries

**UserProfile** (profiles/models.py)
- Fields: user, bio, profile_image, is_premium
- Purpose: Extends user with fitness profile information and premium status
- Relationships: Belongs to One User
- Special: Auto-created via Django signals when user registers

**Delivery** (profiles/models.py)
- Fields: user, full_name, email, phone_number, address_line1, address_line2, city, postal_code, country, created_at
- Purpose: Stores customer shipping addresses for product deliveries
- Relationships: Belongs to One User (ForeignKey)
- Features: Full address property method for formatted addresses

#### Shop 

**Product** (shop/models.py)
- Fields: name, description, price, image, stock
- Purpose: Manages fitness products available for purchase
- Features: 
  - Stock tracking for inventory management
  - Image upload support via AWS S3
  - Low stock warnings (admin feature)

**Order** (shop/models.py)
- Fields: user, created_at, total, paid
- Purpose: Tracks customer purchase transactions
- Relationships: 
  - Belongs to One User
  - Has many OrderItems
- Features: Paid status tracking for order fulfillment

**OrderItem** (shop/models.py)
- Fields: order, product, quantity, price
- Purpose: Individual line items within an order
- Relationships: 
  - Belongs to One Order
  - Belongs to One Product
- Features: Captures price at time of purchase (historical record)

#### Workout Management

**Workout** (workouts/models.py)
- Fields: title, description, difficulty, duration, is_premium
- Purpose: Fitness workout plans for users
- Features:
  - is_premium flag for premium content restriction
  - Difficulty levels (Beginner, Intermediate, Advanced)
- Relationships: Has many Exercises

**Exercise** (workouts/models.py)
- Fields: workout, name, sets, reps, duration
- Purpose: Individual exercises within workout plans
- Relationships: Belongs to One Workout

**Progress** (workouts/models.py)
- Fields: user, exercise, completed, completed_at
- Purpose: Tracks user workout completion progress
- Relationships:
  - Belongs to One User
  - Belongs to One Exercise
- Features: Timestamp tracking for completion history

#### Payments & Premium

**Stripe Integration**
- Used for secure payment processing
- Handles checkout sessions and transactions
- Ensures safe handling of payment data

**Functionality:**
- Users can purchase premium access
- Payments are processed securely via Stripe
- Payment status is stored in the database
- Checkout session management
- Webhook handling for payment confirmation
- Secure metadata storage (order_id, user_id)

**Premium Access Control**
- Managed via UserProfile.is_premium boolean
- Activated automatically after successful Stripe payment
- Admin can manually grant/revoke premium status

#### Contact 

**Contact Form** (pages app)
- Fields: name, email, message
- Purpose: Customer inquiries and support requests
- Features:
  - Email notification to site owner
  - Auto-reply confirmation to customer
  - Gmail SMTP integration

#### Stripe API
- **Purpose**: Secure payment processing for premium subscriptions and product purchases
- **Features**:
  - Checkout session creation and management
  - Secure payment intent handling
  - Payment confirmation and verification
- **Functionality**:
  - Users can purchase premium access
  - Users can buy physical products
  - Payments are processed securely via Stripe
  - Payment status is stored in the database
  - Order confirmation after successful payment

#### Django Allauth (Authentication System)
- **Purpose**: Complete user authentication management
- **Features**:
  - Handles user authentication workflows
  - Email verification and account management
  - Secure login, logout, and registration
  - Password reset functionality
  - Social account integration (optional)
- **Functionality**:
  - Users can register with email confirmation
  - Secure session management
  - Account recovery options

## Design

### Colour Scheme

The platform uses a custom colour palette defined in CSS variables for consistency and easy maintenance.

**Primary Colours:**
- **Primary Red (`#ff4d4d`)** : Used for all primary buttons (Add to Cart, Checkout, Upgrade) and hover states on navigation links. This energetic red reinforces the fitness brand identity.
- **Dark Background (`#1f1f1f`)** : Applied to the navbar, creating a strong, modern contrast against the content area.
- **Accent Light Grey (`#f5f5f5`)** : Serves as the main background colour for the body, reducing eye strain and providing a clean canvas for content.

**Functional & Feedback Colours:**
- **Success Green:** Used for positive indicators, stock availability messages, and successful action confirmations (via Bootstrap alert classes).
- **Danger Red (`#dc3545`)** : Used for error messages, stock warnings when inventory is low, and destructive actions like removing items from the cart.

**Text Colours:**
- **Text Dark (`#333`)** : Primary text colour for body content, ensuring high readability.
- **Text Muted (`#6c757d`)** : Used for secondary information and form placeholders (via Bootstrap).

### Typography

The platform employs a hybrid font strategy combining a modern sans-serif body font with a bold display font for headings.

**Font Stack:**
- **Body Text:** `'Montserrat', sans-serif` - Clean, modern, and highly readable across all devices
- **Headings:** `'Bebas Neue', sans-serif` - Bold, impactful letter-spacing for H1-H4 tags


**Images**
- Workout-related imagery genrated using using Grok.
- Clean and minimal design
- Responsive scaling

**Icons**

The platform uses **Font Awesome 6** icons extensively throughout the interface to improve visual communication and user interaction.

**Navigation Icons:**
| Link | Icon | Purpose |
|------|------|---------|
| Home | `fa-home` | Returns to homepage |
| Workouts | `fa-dumbbell` | Access fitness plans |
| Shop | `fa-store` | Browse fitness products |
| About | `fa-info-circle` | Learn about FitHub |
| Contact | `fa-envelope` | Send inquiries |
| Cart | `fa-shopping-cart` | View shopping cart |

**User Action Icons:**
| Action | Icon | Purpose |
|--------|------|---------|
| Profile | `fa-user` | View user profile |
| Login | `fa-sign-in-alt` | Sign into account |
| Logout | `fa-sign-out-alt` | Sign out of account |
| Register | `fa-user-plus` | Create new account |

**Cart & Checkout Icons:**
| Action | Icon | Purpose |
|--------|------|---------|
| Add to Cart | `fa-shopping-cart` | Add product to cart |
| Remove Item | `fa-trash` | Delete cart item |
| Increase Quantity | `fa-plus` | Add one more unit |
| Decrease Quantity | `fa-minus` | Remove one unit |

**Premium & Feedback Icons:**
| Element | Icon | Purpose |
|---------|------|---------|
| Premium Feature | `fa-crown` | Indicates premium content |
| Success Message | `fa-check-circle` | Confirms successful action |
| Error Message | `fa-exclamation-triangle` | Alerts user to errors |
| Info Message | `fa-info-circle` | Provides helpful information |
| Warning Message | `fa-exclamation-circle` | Warns about important issues |

**Progress Indicators:**
| Indicator | Icon | Purpose |
|-----------|------|---------|
| Workout Progress | `fa-chart-line` | Shows fitness journey progress |
| Loading State | `fa-spinner fa-spin` | Indicates AJAX processing |
| Stock Status | `fa-check-circle` / `fa-times-circle` | Shows product availability |
| Payment Processing | `fa-credit-card` | Indicates Stripe checkout |

## Features  

### Home app

- **Hero Section**

    - Upon opening the site, the user is greeted with a vibrant hero section that clearly defines FitHub as a fitness platform.
    - The hero section features a gradient background (purple to blue) with white text for high contrast.
    - Two call-to-action buttons are prominently displayed: "Start Working Out" and "Shop Now".
    - The hero section encourages users to begin their fitness journey immediately.

    <p align="center">
        <img src="readme-images/features/home_page.png" alt="Hero section with gradient background and CTA buttons" height="180px" width="320px"/>
    </p>

- **Features Section**
    - Three feature cards explain the core benefits of FitHub:
        - **Workout Plans:** Access premium and free workout plans designed by fitness experts
        - **Track Progress:** Monitor your fitness journey and celebrate achievements
        - **Premium Access:** Unlock exclusive content with premium subscription
    - Each card includes a Font Awesome icon (dumbbell, chart-line, crown) for visual appeal
    - Cards have hover effects with shadow for interactive feedback

    <p align="center">
        <img src="readme-images/features/features-section.png" alt="Three feature cards showing workout plans, progress tracking, and premium access" height="200px" width="450px"/>
    </p>

- **Featured Products**
    - The homepage displays up to 2 featured products from the shop database
    - Each product card shows: image, name, price, and "View Details" button
    - Products are fetched dynamically from the Product model
    - Empty state message appears when no products are available
    - "View All Products" button links to the full shop page

    <p align="center">
        <img src="readme-images/features/featured-products.png" alt="Featured products section showing fitness equipment" height="200px" width="450px"/>
    </p>

- **Premium Call-to-Action**
    - Section promotes premium subscription to non-premium users only
    - Shows €19.99/month pricing with list of benefits
    - "Upgrade Now" button links to Stripe checkout
    - **Conditional Display:** Hidden completely for users who already have premium access
    - Guest users see the upgrade prompt with login option

    <p align="center">
        <img src="readme-images/features/premium-cta.png" alt="Premium upgrade section with pricing and benefits" height="180px" width="400px"/>
    </p>

- **Navigation System**
    - Fixed navbar with dark background (`#1f1f1f`) and brand logo
    - Font Awesome icons on all navigation links for improved visual recognition
    - Navigation links include: Home, Workouts, Shop, About, Contact, Cart 
    - User-specific links: Profile/Logout (logged in) or Login/Register (guests)
    - Responsive navbar collapses to hamburger menu on mobile devices

    <p align="center">
        <img src="readme-images/features/navigation.png" alt="Navigation bar with icons for all menu items" height="80px" width="450px"/>
    </p>

- **Interactive Elements**
    - All buttons have hover effects with colour transitions
    - Primary buttons use brand red (`#ff4d4d`) with darker hover state
    - Cards have subtle shadow effects that elevate on hover
    - Loading states during AJAX requests (cart updates)
    - Success/error messages auto-dismiss after 3 seconds

- **Responsive Design**
    - Mobile-first approach using Bootstrap 4.6 grid system
    - Cards stack vertically on screens under 768px
    - Hero section text and buttons adjust spacing on mobile
    - Navigation collapses to hamburger menu with toggle button
    - Images scale appropriately across all device sizes

    <p align="center">
        <img src="readme-images/features/mobile-home.jpeg" alt="Homepage on mobile device showing stacked layout" height="400px" width="200px"/>
    </p>

- **Dynamic Content**
    - Featured products automatically update when new products are added to shop
    - Premium CTA intelligently hides for existing premium members
    - User-specific navigation shows different options based on authentication status
    - Messages display for user actions (add to cart, login required, etc.)

- **Performance Optimizations**
    - Only 2 featured products queried to minimize database load
    - Images use `object-fit: cover` for consistent sizing
    - Bootstrap CDN for faster loading
    - Font Awesome icons loaded via CDN
    - Custom CSS minimal and optimized

- **Accessibility Features**
    - High contrast text on gradient hero section
    - Alt text on all product images
    - Semantic HTML structure
    - Keyboard navigable links and buttons
    - ARIA labels on icon-only elements

- **Future Enhancements**
    - Newsletter signup section (planned)
    - Blog preview showing latest posts (planned)
    - Testimonials section from premium members (planned)
    - Workout progress preview for logged-in users (planned)
    - Animated counters for user statistics (planned)

### Workout app

#### View All Workouts
- Users can browse all available workout plans from the navigation menu
- Workouts are displayed in a responsive card grid layout
- Each workout card shows title, difficulty level, duration, and premium status
- Premium workouts are clearly marked with a crown icon for non-subscribers

<p align="center">
    <img src="readme-images/features/workouts_page.png" alt="Workouts list page showing premium and free workouts" height="250px" width="500px"/>
</p>

#### Detailed Workout Pages
- Clicking any workout opens a detailed page with complete information
- Page displays: title, description, difficulty level, duration, and exercise list
- Premium workouts show a locked message for non-premium users
- Premium users see full exercise details with sets and reps

<p align="center">
    <img src="readme-images/features/workout_withexercise and progress.png" alt="Detailed workout page with exercises" height="300px" width="500px"/>
</p>

#### Exercises with Sets and Reps
- Each workout contains multiple exercises
- Exercises display name, sets, reps, and duration
- Users can mark individual exercises as complete
- Completion status is saved to user profile

#### Premium Workout Restriction
- Premium workouts are only accessible to users with active subscription
- Non-premium users see upgrade prompt with link to premium checkout
- Backend verification prevents URL bypass attempts
- Premium status is checked on every workout access

<p align="center">
    <img src="readme-images/features/Premium workouts.png" alt="Premium workout locked message" height="200px" width="400px"/>
</p>

---

### Progress Tracking

#### Mark Exercises as Complete
- Registered users can check off exercises as they complete them
- Checkboxes provide instant visual feedback
- Completion status is saved to database immediately

#### Stored Per User
- Each user has their own progress tracking
- Progress data persists across sessions
- Users can see their completed workouts history

#### Dynamic Updates
- Progress updates without page refresh (AJAX)
- Dashboard shows real-time completion percentage
- Visual indicators show progress at a glance

<p align="center">
    <img src="readme-images/features/progress.png" alt="Progress tracking dashboard showing completion percentage" height="200px" width="450px"/>
</p>

---

### Authentication System (Django Allauth)

#### Registration and Login
- Users can create accounts with email and password
- Registration form validates input and creates user profile automatically
- Login form with remember me option
- Password reset functionality via email

<p align="center">
    <img src="readme-images/features/register_page.png" alt="Login page" height="250px" width="400px"/>
    <img src="readme-images/features/login_page.png" alt="Registration page" height="250px" width="400px"/>
</p>

#### Email Verification
- New users receive verification email upon registration
- Accounts must verify email before accessing premium features
- Verification links expire for security

#### Secure Account Management
- Users can update profile information
- Change password functionality
- Secure session management
- Logout option available from navigation

---

### Payments app

#### Premium Access Purchase
- Users can purchase monthly premium subscription for €19.99
- Premium checkout page displays plan details and benefits
- One-click payment via Stripe

<p align="center">
    <img src="readme-images/features/premium-checkout.png" alt="Premium checkout page with Stripe" height="250px" width="450px"/>
</p>

#### Secure Checkout
- Stripe handles all payment processing (PCI compliant)
- Users never enter payment details on FitHub servers
- Test mode available for development

#### Payment Validation
- Payment success redirects to confirmation page
- Premium status activated immediately after successful payment
- Admin can manually manage premium status via admin panel

<p align="center">
    <img src="readme-images/features/payment-success.png" alt="Payment success confirmation page" height="200px" width="450px"/>
</p>

---

### Shop app

#### Browse Products
- All products displayed in responsive grid layout
- Each product shows: image, name, price, and stock status
- Low stock warning appears when inventory is low (<10 units)
- Out of stock products are clearly marked

<p align="center">
    <img src="readme-images/features/shop_page.png" alt="Shop page showing fitness products" height="250px" width="500px"/>
</p>

#### Product Details
- Click any product to view detailed information
- Page shows: full description, price, stock availability
- Quantity selector with stock limit validation
- Add to cart button with visual feedback

<p align="center">
    <img src="readme-images/features/product-detail.png" alt="Product detail page with quantity selector" height="300px" width="450px"/>
</p>

#### Shopping Cart
- Add/remove products from cart
- Update quantities with +/- buttons (AJAX)
- Real-time total price calculation
- Cart persists in session for guest users
- Stock validation prevents over-purchasing

<p align="center">
    <img src="readme-images/features/cart_page_withitem.png" alt="Shopping cart page with quantity controls" height="250px" width="500px"/>
</p>

#### Checkout Process
- Delivery address collection before payment
- Form includes: name, email, phone, address, city, postal code, country
- Order summary shows all items and total
- Login required before checkout

<p align="center">
    <img src="readme-images/features/checkout-form.png" alt="Checkout delivery form" height="300px" width="450px"/>
</p>

#### Order Confirmation
- Users receive order confirmation on success page
- Order details saved to database
- Admin can view all orders in admin panel
- Stock automatically reduced after purchase

<p align="center">
    <img src="readme-images/features/order-success.png" alt="Order confirmation page" height="200px" width="450px"/>
</p>

---

### Profile app

#### User Profiles
- Each registered user has a dedicated profile page
- Profile displays: username, bio, profile image, premium status
- Users can upload profile picture
- Bio text area for personal description

<p align="center">
    <img src="readme-images/features/profile_page_logedin.png" alt="User profile page" height="250px" width="450px"/>
</p>

#### Premium Status Tracking
- Profile clearly shows if user has premium access
- Premium badge displayed for subscribers
- Upgrade button shown for non-premium users
- Premium status unlocks premium workout content

#### Edit Profile
- Users can update their bio and profile image
- Form validates image uploads
- Changes reflect immediately on profile page

<p align="center">
    <img src="readme-images/features/edit-profile.png" alt="Edit profile form" height="250px" width="400px"/>
</p>

---

### Admin Management

#### Product Management
- Admin can add, edit, and delete products via Django admin
- Stock levels can be updated from product list
- Low stock warning column highlights products needing restock
- Product images upload to AWS S3

#### Order Management
- View all customer orders with details
- Filter orders by paid status and date
- See which products were ordered
- Customer delivery addresses visible

#### Premium User Management
- View all users and their premium status
- Manually grant or revoke premium access
- Filter users by premium status
- Search users by username or email

#### Delivery Address Management
- View all customer delivery addresses
- Addresses include full name, phone, and complete address
- Created timestamp for reference
- Search deliveries by customer name or city

<p align="center">
    <img src="readme-images/features/admin-panel.png" alt="Django admin panel showing orders and products" height="250px" width="500px"/>
</p>

---

### Pages app

#### About Page
- Learn about FitHub platform
- Describes services offered: workouts, shop, premium content
- Subscription benefits explained
- Responsive and readable on all devices

<p align="center">
    <img src="readme-images/features/about_page.png" alt="About page" height="200px" width="450px"/>
</p>

#### Contact Form
- Users can send messages to site owner
- Form fields: name, email, message
- Email notification sent to admin via Gmail SMTP
- Success message displayed on submission

<p align="center">
    <img src="readme-images/features/contact_page.png" alt="Contact form page" height="250px" width="450px"/>
</p>
---

## Testing

- #### Testing.
  - The testing section for this site is located at the following link.
    - [Testing file](TESTING.md)

## Technologies used.

- The application was built on the Django full-stack framework.
- For each section of the site a Django app was created.
- Each app then has a views.py, urls.py file to create the pages it needs.
- Then to create the database models a models.py file is used.
- If there are any forms needed they are then created in the forms.py file.
- Stripe has been used for the payment function.
- Heroku was used to deploy the application.
- Amazon AWS was used to store. the static files and the image files.

### Languages Used.

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

  - HTML5 was used to create the content and base of each page.

- [CSS3](https://en.wikipedia.org/wiki/CSS)

  - CSS3 was used to then style the page and make it responsive through media queries, and interactive through using CSS transitions.

- [javaScript](https://en.wikipedia.org/wiki/JavaScript)
  - javaScript was used throughout the website to make the site interactive.

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  - Python was used to build the backend functionality of the web app.

### Django and Django extensions used

- [Django](https://www.djangoproject.com/)
  - Django was used to create the project.

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
  - Django allauth was used to create the user sign-in function for the site.

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  - Django Crispy Forms were used to utilise the bootstrap form classes.

- [Django Coverage](https://pypi.org/project/django-coverage/)

  - Django Coverage was used when testing to form a testing report.


### Frameworks Libraries and Programs.

- [Stripe](https://stripe.com/ie)

  - CStripe has been used for the payment section of the site.

- [Heroku](https://signup.heroku.com/)

  - Heroku was used to deploy the website.

- [Amazon AWS](https://aws.amazon.com/)

  - Amazon AWS was used to store the static files and the images for the site.

- [Gunicorn](https://gunicorn.org/)

  - Gunicorn was used for deploying the project to Heroku.

- [Google Fonts](https://fonts.google.com/)

  - I imported the Mulish font from google fonts and used it consistently across the site.

- [Bootstrap 5](https://getbootstrap.com/)

  - Bootstrap 5 was used for its grid system and its form inputs and its helper classes.

- [Quick Database Diagrams](https://www.quickdatabasediagrams.com/)

  - I used quick database diagrams to make a diagram of my database schema.

- [Github](https://github.com/)

  - Github was used to create and store the project repository.

- [Balsamiq](https://balsamiq.com/)

  - Balsamiq was used to create Wireframes for the project during the initial planning stage.


### Deployment.

#### Github, Heroku, and Amazon AWS.

- #### Project setup.
 - The project was set up on GitHub.
  - I then named my repository and created it.
  - once it is created i created differnt issue and added it to project. 
  - Then i started create files and folders and start coding the project.
  - Throughout the project, I used git to add my changes to version control in GitHub.
  - To commit I added the file to the staging area with the 
    ```
        git add <filename>
    ```
    ```
        git commit -m "<commit message>"
    ```
    ```
        git push
    ```
 
- #### Deployment to Heroku

  Once the app was ready I deployed it to Heroku by following these steps.

- **Create an app on the Heroku website.**
    - Firstly I clicked on the new button.
    - Then I clicked on the create a new app.
    - I then gave my app a name and chose my current region.
    - I then selected create app.

- **Set up Postgres Database**
  - Heroku
    - In the app resources section I searched for Postgres
    - I then choose to add to the project and, choosing the free plan.
    - To use Postgres we need to install 2 dependencies.
        - dj_database_url
        - psycopg2

  - **In Project.**
    - I first installed the two packages needed 

    - 
        ``` 
            pip3 install dj_database_url
        ```
    -
        ```
            pip3 install psycopg2_binary
        ```

    - I then made sure to add them to the requirements.txt file
    -
        ```
        pip3 freeze > requirements.txt
        ```
    - Then in settings.py I imported dj_database_url
    - 
        ``` python
        import dj_database_url
        ```
    - I then commented out the current database settings.
    - I then replaced it with the settings for the Postgres database.
    -
        ``` python
            DATABASES = {
                'default': dj_database_url.parse('DATABASE_URL')
            }
        ```
    - Get your database URL from your app config settings. (I haven't shown it above as its and environmental variable and shouldn't be shown in version control)

    - Once this is set up we need to migrate our models to the new database.
    - 
        ``` 
            python3 manage.py migrate
        ```

    - Once this was done I then created a superuser.
    - 
        ```
            python3 manage.py createsuperuser
        ```
    
    - I then committed my changes making sure to remove my database URL beforehand so it isn't saved in version control.

    - I then created an if-else statement in the settings.py to use Postgres if the DATABASE_URL variable is available and if not use the default database

    - 
        ``` python
            if "DATABASE_URL" in os.environ:
                DATABASES = {
                    "default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
                }
            else:
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': BASE_DIR / 'db.sqlite3',
                    }
                }
        ```
    
    -The Postgres database is now ready for use.

  - **Gunicorn**
    - For our app to work we need to install Greenunicorn.
    - To install 
    - 
        ```
        pip3 install Gunicorn
        ```
    - We then need to create a Procfile to let Heroku know how to run the app.
    -
        ``` 
            touch Procfile
        ```
    - Then in our Procfile place the following code.
    -
        ```
            web: gunicorn <app name>.wsgi:application
        ```

  - **Heroku in the command line.**
    - I then logged into Heroku using the terminal.
    -
        ```
            heroku login -i
        ```
    - Then I temporarily disabled the static files until they have been set up on Amazon Aws.
    -
        ```
            heroku config:set DISABLE_COLLECTSTATIC=1 --app <app name>
        ```
        - Use the --app command if you have more than one Heroku app.
    - Then in settings I added Heroku into allowed hosts, and localhost so my project can still be run locally.
    -
        ``` python
            ALLOWED_HOSTS = ["<heroku app name>.herokuapp.com", "localhost"]
        ```
    - My changes were then committed to Github.
    - Then I set up pushing to Heroku
    -
        ```
            heroku git:remote -a <heroku app name>
        ```
    - Then we push the project to Heroku
    -
        ```
            git push heroku master
        ```

    - Heroku will now build your app.

  - **Heroku Website**

    - I then connected my app to GitHub by opening the Deploy section.
    - I then searched for my repository.
    - Once found I connected and then enabled Automatic Deploys
    - This now means that any changes pushed to GitHub will be automatically pushed to Heroku as well.

- #### Amazon AWS

  - Amazon AWS was used to store both static files and media files.
  - Firstly I created an AWS account and worked through the sign-up process. Once my account was set up I was able to set my project up on AWS.

  - **Create a bucket.**

    - Create the bucket
        - First thing was to create a new bucket on the AWS S3 service.
        - From the main dashboard search for S£ and then click to get started.
        - Click on the Create bucket button.
        - Give the bucket a name and select your region.
        - Then uncheck the block public access and acknowledge that the bucket will now be public.
        - Then click create bucket.
    
    - Bucket settings.
        - Properties
            - Navigate to the bucket properties settings.
            - Turn on static website hosting.
            - In the index and error add index.html and error.html.
            - Click Save.
        - Permissions
            - Click on the buckets Permissions tabs.
            - Firstly paste in the following cors config.
            - 
                ```
                [
                    {
                        "AllowedHeaders": [
                            "Authorization"
                        ],
                        "AllowedMethods": [
                            "GET"
                        ],
                        "AllowedOrigins": [
                            "*"
                        ],
                        "ExposeHeaders": []
                    }
                    ]
                ```
            - Then in the bucket policy tap, click on generate policy.
            - Policy
            - Select S3 bucket policy
            - Add * to the principal field to select all principals
            - Set the action to get object.
            - Paste in your ARN which is available on the previous page.
            - Click, add statement
            - Then click, generate policy.
            - Now copy and paste your new policy into the bucket policy.
            - Add /* onto the end of the resources key
            - Click Save.
        - Access control list
        - In the access control list tab set the list objects permission to everyone.
    
   - **Create a User.**

     - To create a user for the bucket we need to use another Amazon service.
     - Back in the main dashboard search for IAM and select it.
     
     - Create a Group.
       - Firstly we need to create a group to put our user in.
       - Click create a new group and name it.
       - Click through to the end and save the group.
       - Create a policy.
         - In our group click, policy and then, create policy.
         - Select the JSON tab and then import managed policies.
         - Search S3 and select AmazonS3FullAccess and import.
         - In the resources section paste in our arn from before.
         - click through to review the policy.
         - Fill in name and description and then click generate policy.
       - Back in your group click permission and then attach the policy.
       - Find the policy you've just created and attach it.
    
     - Create the User.
       - Select Users from the sidebar and then click, add user.
       - Create a user name and select programmatic access then click next.
       - Then select your group to add your user to.
       - Click through to the end and then click create user.
       - ** Make sure to now download the CSV file as it contains the users keys needed to access from our app.**

  - **Connecting to Django**
    
    - Once our AWS has been set up we now need to connect it to Django.
    - Firstly two packages are needed.
      - boto 3
      - Django storages
    - Firstly install these packages.
    -
        ```
            pip3 install boto3
            pip3 install django-storages
        ```
    - Then add to our requirements.
    -
        ```
            pip3 freeze > requirements.txt
        ```
    - We then add storages into our installed apps in settings.py
    - We then add the following settings to our settings.py
    - We create an environmental variable to only run this code when on Heroku. "USE_AWS"
    -
        ``` python
            if "USE_AWS" in os.environ:

                # Bucket Config
                AWS_STORAGE_BUCKET_NAME = '<bucket name>'
                AWS_S3_REGION_NAME = '<your region>'
                AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
                AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
                AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

                # static and media file storage
                STATICFILES_STORAGE = 'custom_storages.StaticStorage'
                STATICFILES_LOCATION = 'static'
                DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
                MEDIAFILES_LOCATION = 'media'

                # Override static and media URLs in production
                STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
                MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
        ```
    - Then back in Heroku we click the settings and reveal config vars.
    - Then set up the environmental variables needed.
    - We then create a custom_storages.py to tell Django that in production we want to use s3 to store our static and media files.
    - We Firstly need to import S3Boto3Storage.
    - then we set up our new classes to tell Django where to store the files.
    -
        ``` python
            class StaticStorage(S3Boto3Storage):
                location = settings.STATICFILES_LOCATION


            class MediaStorage(S3Boto3Storage):
                location = settings.MEDIAFILES_LOCATION
        ```
    - Once all the settings are done we can now push to GitHub and Heroku.

  - **Add our media to AWS.**
  
    - The final step is to add our media to AWS.
    - In your bucket create a new folder called media.
    - Select upload and add your image files.
    - Then select to grant public access.
    - And then upload the files.

#### Setting up locally

  - To set the project up locally you can follow these steps.
    
    - Log in to your GitHub account and navigate to the Repositories section.

    - Click the New button to create a new repository.

    - Give your repository a name (e.g., fithub) and choose public/private visibility.

    - Once the repository is created, copy the repository URL from the Code dropdown button.

      - <p align="center"><img src="readme-images/deployment/deployment.png" alt="deployment for github" height="200px" width="350px"/></p>
    
    - Open Visual Studio Code on your local machine.

    - Open the terminal in VS Code (Terminal → New Terminal or Ctrl + ``).

    - Clone the repository by pasting the code you copied from GitHub:

    - Alternatively, you can clone it into your repository using the following command.

      - ```
            git clone https://github.com/eandachew/fithub
        ```
    
    - Navigate into the project directory:

    
      ```
            pip3 install -r requirements.txt
      ```
    
    - You must then set up the following environment variables to use the full functionality of the site.

      - DANGO_SECRET_KEY = your secret key.
      - STRIPE_PUBLIC_KEY = your stripe public key.
      - STRIPE_SECRET_KEY = your stripe secret key.
      - STRIPE_WEBHOOK_SECRET = your stripe webhook secret.
      - IN_DEVELOPMENT = True

      - Your stripe variables can be found on your stripe dashboard.
      - You can generate a Django secret key here. [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
    
    - You will then need to migrate the database models to set up your database.
    - 
      - Check first
        ```
            python3 manage.py makemigrations --dry-run
        ```
       -  Then make migrations.
            ```
                python3 manage.py makemigrations
            ```
       - Check the migration plan
            ```
                python3 manage.py migrate --plan
            ```
       - Then finally migrate
            ```
                python3 manage.py migrate
            ```

     - Then create your superuser to access the admin section.
      -
        ```
            python3 manage.py createsuperuser
        ```

        - Following the prompts.

    - Once these steps have been followed you can then run the project by using the following command.

        - 
            ```
                python3 manage.py runserver
            ```
## Credits.

### Code.

- #### Kevin Powell Youtube video.
    - [Fade + slide in nav list items one at a time](https://www.youtube.com/watch?v=xkKjrH3pRfg&list=WL&index=3&t=1028s)
        - This youtube walkthrough help me to design and animate my navigation menu. I've adapted the code to suit my site.

- #### Stack Overflow 

    - [Sending POST data with fetch](https://stackoverflow.com/questions/6396101/pure-javascript-send-post-data-without-a-form)
        - I used code from the above StackOverflow article to help with sending post data using fetch in javascript.

    - [Messages extra tags](https://stackoverflow.com/questions/15017706/how-to-display-multiple-django-messages-in-one-page)
        - I used the above article to help with only showing the cart items with some successful messages.


### Content

- All Text for the website was written by myself.

### Media

- [Grok](https://grok.com)
    - All images for the website were obtained from Unsplash.

### Acknowledgements

- Code Institute for getting me to this point
