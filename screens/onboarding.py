import streamlit as st

def render():
    st.markdown("""
    <style>
        /* Sparkling, multi-color dark background (calm + premium) */
        [data-testid="stAppViewContainer"]{
            min-height: 100vh;
            position: relative;
            overflow: hidden;

            /* Base: deep dark gradient */
            background:
              radial-gradient(1000px 700px at 18% 12%, rgba(99,102,241,0.24) 0%, rgba(99,102,241,0.00) 60%),
              radial-gradient(950px 650px at 82% 18%, rgba(124,58,237,0.20) 0%, rgba(124,58,237,0.00) 58%),
              radial-gradient(900px 650px at 45% 88%, rgba(16,185,129,0.10) 0%, rgba(16,185,129,0.00) 60%),
              radial-gradient(900px 650px at 86% 82%, rgba(59,130,246,0.10) 0%, rgba(59,130,246,0.00) 58%),
              linear-gradient(135deg, #060511 0%, #0b0920 25%, #170c2c 50%, #24124c 75%, #0c0a18 100%);
        }

        /* --- Sparkle layer (soft bokeh dots) --- */
        [data-testid="stAppViewContainer"]::before{
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
            opacity: 0.55;
            filter: blur(0.2px);

            /* multiple tiny radial “lights” */
            background:
              radial-gradient(4px 4px at 12% 22%, rgba(255, 99, 132, 0.22) 0%, rgba(255, 99, 132, 0) 70%),
              radial-gradient(3px 3px at 20% 68%, rgba(99, 102, 241, 0.22) 0%, rgba(99, 102, 241, 0) 70%),
              radial-gradient(4px 4px at 32% 35%, rgba(34, 211, 238, 0.18) 0%, rgba(34, 211, 238, 0) 70%),
              radial-gradient(3px 3px at 48% 80%, rgba(16, 185, 129, 0.18) 0%, rgba(16, 185, 129, 0) 70%),
              radial-gradient(4px 4px at 62% 28%, rgba(168, 85, 247, 0.20) 0%, rgba(168, 85, 247, 0) 70%),
              radial-gradient(3px 3px at 74% 56%, rgba(251, 191, 36, 0.16) 0%, rgba(251, 191, 36, 0) 70%),
              radial-gradient(4px 4px at 88% 30%, rgba(59, 130, 246, 0.18) 0%, rgba(59, 130, 246, 0) 70%),
              radial-gradient(3px 3px at 86% 78%, rgba(244, 114, 182, 0.18) 0%, rgba(244, 114, 182, 0) 70%);
            animation: sparkleDrift 18s ease-in-out infinite;
        }

        /* --- Vignette + subtle grain for premium feel --- */
        [data-testid="stAppViewContainer"]::after{
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;

            background:
              radial-gradient(1200px 750px at 50% 45%,
                rgba(0,0,0,0.00) 0%,
                rgba(0,0,0,0.22) 55%,
                rgba(0,0,0,0.55) 100%),
              repeating-radial-gradient(circle at 18% 26%,
                rgba(255,255,255,0.05) 0px,
                rgba(255,255,255,0.00) 2px,
                rgba(0,0,0,0.00) 6px);
            opacity: 0.18;
            mix-blend-mode: overlay;
        }

        @keyframes sparkleDrift {
            0%   { transform: translate3d(0,0,0) scale(1); opacity: 0.45; }
            50%  { transform: translate3d(10px,-8px,0) scale(1.03); opacity: 0.65; }
            100% { transform: translate3d(0,0,0) scale(1); opacity: 0.45; }
        }

        /* Accessibility: if user prefers reduced motion, stop animations */
        @media (prefers-reduced-motion: reduce) {
            [data-testid="stAppViewContainer"]::before {
                animation: none !important;
            }
        }

        /* MINIMAL 6 breathing bubbles (your existing) */
        .bubble-breath {
            position: absolute;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(99,102,241,0.12) 0%, rgba(16,185,129,0.08) 70%, transparent 100%);
            border: 1px solid rgba(99,102,241,0.06);
            animation: breathLight 9s ease-in-out infinite;
            box-shadow: 0 0 12px rgba(99,102,241,0.08);
            z-index: 1;
            pointer-events: none;
        }
        @keyframes breathLight {
            0%, 100% { transform: scale(1); opacity: 0.4; }
            25% { transform: scale(1.25); opacity: 0.65; }
            50% { transform: scale(1.45); opacity: 0.85; }
            75% { transform: scale(1.25); opacity: 0.65; }
        }

        .sanctuary-glass {
            background: rgba(26, 26, 46, 0.80);
            backdrop-filter: blur(25px);
            border-radius: 28px;
            border: 1px solid rgba(71, 71, 99, 0.40);
            padding: 3rem 2.5rem;
            max-width: 520px;
            margin: 2rem auto;
            position: relative;
            z-index: 10;
            box-shadow:
              0 28px 56px rgba(0,0,0,0.55),
              0 0 0 1px rgba(99,102,241,0.10) inset,
              0 0 40px rgba(124,58,237,0.10);
        }

        .hero-calm {
            color: #f8fafc;
            font-size: 3rem;
            font-weight: 500;
            text-align: center;
            margin-bottom: 0.8rem;
            line-height: 1.1;
        }

        .mood-serene {
            width: 70px; height: 70px;
            border-radius: 20px;
            display: flex; align-items: center; justify-content: center;
            font-size: 2.1rem;
            background: rgba(71, 71, 99, 0.40);
            border: 1px solid rgba(148, 163, 184, 0.30);
            backdrop-filter: blur(12px);
            transition: all 0.4s ease;
            box-shadow: 0 8px 24px rgba(0,0,0,0.30);
        }
        .mood-serene:hover {
            background: rgba(99, 102, 241, 0.25);
            border-color: rgba(99, 102, 241, 0.40);
            transform: translateY(-4px);
            box-shadow: 0 16px 32px rgba(99,102,241,0.25);
        }

        .breath-guide {
            text-align: center;
            margin: 2.5rem 0;
            color: #94a3b8;
        }
        .breath-circle {
            width: 95px; height: 95px;
            border-radius: 50%;
            margin: 1rem auto;
            background: conic-gradient(from 0deg, #10b981, #34d399, #059669, #10b981);
            border: 2px solid rgba(16,185,129,0.40);
            animation: breathCycle 6s ease-in-out infinite;
            box-shadow: 0 0 36px rgba(16,185,129,0.40);
        }
        @keyframes breathCycle {
            0% { transform: scale(1) rotate(0deg); }
            25% { transform: scale(1.35) rotate(90deg); }
            50% { transform: scale(1.55) rotate(180deg); }
            75% { transform: scale(1.35) rotate(270deg); }
            100% { transform: scale(1) rotate(360deg); }
        }
        .breath-text {
            font-size: 1.1rem;
            font-weight: 500;
            margin-top: 1rem;
            min-height: 1.5rem;
        }
    </style>
    """, unsafe_allow_html=True)

    # Your 6 bubbles (unchanged positions)
    st.markdown("""
    <div class="bubble-breath" style="left:15%; top:20%; width:28px; height:28px; animation-delay:0s;"></div>
    <div class="bubble-breath" style="left:75%; top:25%; width:24px; height:24px; animation-delay:2s;"></div>
    <div class="bubble-breath" style="left:25%; top:60%; width:26px; height:26px; animation-delay:4s;"></div>
    <div class="bubble-breath" style="right:20%; top:70%; width:22px; height:22px; animation-delay:1s;"></div>
    <div class="bubble-breath" style="left:80%; bottom:30%; width:25px; height:25px; animation-delay:3s;"></div>
    <div class="bubble-breath" style="left:10%; bottom:60%; width:27px; height:27px; animation-delay:5s;"></div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sanctuary-glass">', unsafe_allow_html=True)

    st.markdown('<h1 class="hero-calm">Unsaid</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#cbd5e1; font-size:1.2rem; text-align:center; margin-bottom:2.5rem; line-height:1.6; font-weight:400;">'
        "A space for what you can't say out loud."
        '</p>', unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    moods = ["😔", "😟", "😰", "😐", "😊", "🥰"]
    for i, mood in enumerate(moods):
        with (col1, col2, col3)[i % 3]:
            st.markdown(f'<div class="mood-serene">{mood}</div>', unsafe_allow_html=True)

    st.markdown('<div class="breath-guide">', unsafe_allow_html=True)
    st.markdown('<div class="breath-circle"></div>', unsafe_allow_html=True)
    st.markdown('<div class="breath-text">🫁 Breathe In... → 💨 Out... → 😌 Rest</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        '<div style="text-align:center; color:#94a3b8; font-size:0.92rem; margin:2.5rem 0; line-height:1.6;">'
        '🛡️ Unsaid provides emotional support only and does not offer medical advice or diagnosis.'
        '</div>',
        unsafe_allow_html=True
    )

    trusted_contact = st.text_input(
        "Trusted contact (optional)",
        placeholder="Email/phone for crisis support only",
        key="trusted_contact",
        help="Only used with explicit consent"
    )

    if st.button("Begin", key="begin_perfect"):
        st.session_state.trusted_contact = trusted_contact
        st.session_state.page = "mood_checkin"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        '<div style="text-align:center; color:#64748b; font-size:0.85rem; margin-top:3rem; padding-top:2rem; border-top:1px solid rgba(71,71,99,0.3);">'
        '💾 Everything stays private on your device'
        '</div>',
        unsafe_allow_html=True
    )
