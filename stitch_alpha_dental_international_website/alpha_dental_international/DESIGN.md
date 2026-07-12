---
name: Alpha Dental International
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#45464d'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#006b5f'
  on-secondary: '#ffffff'
  secondary-container: '#6df5e1'
  on-secondary-container: '#006f64'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#0d1c2d'
  on-tertiary-container: '#768599'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#71f8e4'
  secondary-fixed-dim: '#4fdbc8'
  on-secondary-fixed: '#00201c'
  on-secondary-fixed-variant: '#005048'
  tertiary-fixed: '#d4e4fa'
  tertiary-fixed-dim: '#b9c8de'
  on-tertiary-fixed: '#0d1c2d'
  on-tertiary-fixed-variant: '#39485a'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-xl:
    fontFamily: Source Serif 4
    fontSize: 60px
    fontWeight: '600'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Source Serif 4
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Source Serif 4
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Source Serif 4
    fontSize: 30px
    fontWeight: '500'
    lineHeight: 38px
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1280px
  gutter: 24px
  margin-desktop: 80px
  margin-mobile: 20px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-gap: 120px
---

## Brand & Style
The brand personality is clinical excellence met with boutique hospitality. This design system targets high-net-worth individuals and health-conscious professionals who prioritize precision and comfort. 

The design style is **Minimalist-Modern with Tonal Layering**. It leverages high-density whitespace to evoke a sense of sterile cleanliness, balanced by deep blue tones to establish authority and trust. The emotional response should be one of "calm confidence"—removing the traditional anxiety associated with dental visits through airy layouts, high-end editorial typography, and soft, tactile UI elements.

## Colors
The palette is rooted in a "Clinical Luxury" spectrum:
- **Primary (Midnight Navy):** Used for primary navigation, headings, and high-impact buttons to convey stability and institutional trust.
- **Secondary (Medical Teal):** Used sparingly for calls-to-action, success states, and subtle accents to provide a modern, sterile yet fresh energy.
- **Tertiary (Soft Silver):** Reserved for borders, dividers, and disabled states, mimicking the brushed metal of high-end medical equipment.
- **Neutral (Arctic White & Slate):** The background is primarily `#FFFFFF`, with `#F8FAFC` used for section staggering to maintain depth without clutter.

## Typography
The typographic hierarchy relies on the contrast between the authoritative, scholarly feel of **Source Serif 4** and the precise, contemporary clarity of **Hanken Grotesk**.

- **Headlines:** Use Source Serif 4 with tight letter-spacing for a premium editorial look. Large display sizes should be centered for landing pages or left-aligned for informational content.
- **Body:** Use Hanken Grotesk for maximum legibility in patient forms and service descriptions. Maintain generous line heights to prevent visual fatigue.
- **Labels:** Small caps or increased letter spacing should be applied to Hanken Grotesk when used for eyebrow headlines or table headers to denote categorization.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy on desktop to maintain an ultra-premium, controlled aesthetic. 

- **Desktop:** 12-column grid with a 1280px max-width. Use large vertical gaps (120px+) between sections to allow content to "breathe."
- **Tablet:** 8-column grid with 40px side margins.
- **Mobile:** 4-column fluid grid.
- **Rhythm:** Use an 8px base unit. Component internal padding should favor "airy" vertical spacing (e.g., 16px top/bottom for input fields) to reinforce the boutique feel.

## Elevation & Depth
Depth is achieved through **Ambient Shadows** and **Tonal Layers**. Avoid heavy borders.

- **Level 1 (Surfaces):** Use a very soft, diffused shadow (0px 4px 20px rgba(15, 23, 42, 0.05)) for cards and containers.
- **Level 2 (Interaction):** On hover, elevate elements slightly by increasing shadow spread and shifting the Y-offset (0px 10px 30px rgba(15, 23, 42, 0.08)).
- **Level 3 (Overlays):** Modals and dropdowns use a "Glassmorphism" hint with a backdrop-blur (12px) and a thin 1px border in `#94A3B8` at 20% opacity.

## Shapes
This design system utilizes **Soft** roundedness. Precision is key in dentistry, so while sharp corners feel too aggressive, fully rounded "pill" shapes feel too casual. A consistent 0.25rem (4px) radius on buttons and 0.75rem (12px) on cards provides a professional, "architectural" softened edge.

## Components
- **Buttons:** Primary buttons are Solid Midnight Navy with white text. Secondary buttons use a "Ghost" style with a Medical Teal border.
- **Input Fields:** Use a floating label pattern with a 1px bottom border only in the default state, transitioning to a full-outline in Medical Teal when focused to symbolize precision.
- **Cards:** White backgrounds with the Level 1 Ambient Shadow. Use high-quality photography of the clinic or medical staff as a top-flush image.
- **Chips:** Used for "Available Appointments" or "Specialties." Soft Teal background (`#F0FDFA`) with Teal text (`#115E59`).
- **Lists:** Use custom iconography (medical-grade line icons) instead of standard bullets. Lines should be 1.5px thick.
- **Appointment Scheduler:** A high-contrast calendar component using generous cell padding and a clear "Today" highlight in Medical Teal.