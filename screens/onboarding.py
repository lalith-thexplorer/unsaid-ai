import streamlit as st

def render():
    st.markdown("""
    <style>
        /* ✅ Updated: richer, more aesthetic multi-layer gradient (still dark + calm) */
        [data-testid="stAppViewContainer"] {
            background:
  radial-gradient(900px 600px at 12% 18%, rgba(99,102,241,0.22) 0%, rgba(99,102,241,0.00) 60%),
  radial-gradient(850px 520px at 88% 22%, rgba(124,58,237,0.18) 0%, rgba(124,58,237,0.00) 58%),
  radial-gradient(900px 520px at 40% 88%, rgba(16,185,129,0.10) 0%, rgba(16,185,129,0.00) 60%),
  radial-gradient(820px 520px at 78% 78%, rgba(59,130,246,0.10) 0%, rgba(59,130,246,0.00) 55%),
  linear-gradient(135deg, #070612 0%, #0d0a1f 22%, #1a0f2e 48%, #24124c 72%, #120f2a 100%);

        }

        /* MINIMAL 6 breathing bubbles */
        .bubble-breath {
            position: absolute;
            border-radius: 50%;
            background: radial-gradient(circle,
                rgba(99,102,241,0.12) 0%,
                rgba(16,185,129,0.08) 70%,
                transparent 100%);
            border: 1px solid rgba(99,102,241,0.06);
            animation: breathLight 9s ease-in-out infinite;
            box-shadow: 0 0 12px rgba(99,102,241,0.08);
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
            box-shadow: 0 28px 56px rgba(0,0,0,0.5);
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

        .btn-serene {
            background: linear-gradient(135deg, #6366f1, #7c3aed);
            border: none;
            border-radius: 20px;
            padding: 1.2rem 3rem;
            font-size: 1.15rem;
            font-weight: 500;
            color: white;
            width: 100%;
            box-shadow: 0 12px 32px rgba(99,102,241,0.30);
            transition: all 0.3s ease;
        }
        .btn-serene:hover {
            transform: translateY(-2px);
            box-shadow: 0 18px 40px rgba(99,102,241,0.40);
        }
    </style>
    """, unsafe_allow_html=True)

    # 6 bubbles (keep your exact positions)
    st.markdown("""
    <div class="bubble-breath" style="left:15%; top:20%; width:28px; height:28px; animation-delay:0s;"></div>
    <div class="bubble-breath" style="left:75%; top:25%; width:24px; height:24px; animation-delay:2s;"></div>
    <div class="bubble-breath" style="left:25%; top:60%; width:26px; height:26px; animation-delay:4s;"></div>
    <div class="bubble-breath" style="right:20%; top:70%; width:22px; height:22px; animation-delay:1s;"></div>
    <div class="bubble-breath" style="left:80%; bottom:30%; width:25px; height:25px; animation-delay:3s;"></div>
    <div class="bubble-breath" style="left:10%; bottom:60%; width:27px; height:27px; animation-delay:5s;"></div>
    """, unsafe_allow_html=True)

    # Main card
    st.markdown('<div class="sanctuary-glass">', unsafe_allow_html=True)

    st.markdown('<h1 class="hero-calm">Unsaid</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#cbd5e1; font-size:1.2rem; text-align:center; margin-bottom:2.5rem; line-height:1.6; font-weight:400;">'
        'A space for what you can&#x27;t say out loud.'
        '</p>',
        unsafe_allow_html=True
    )

    # Mood badges (same layout as your current code)
    col1, col2, col3 = st.columns(3)
    moods = ["😔", "😟", "😰", "😐", "😊", "🥰"]
    for i, mood in enumerate(moods):
        with (col1, col2, col3)[i % 3]:
            st.markdown(f'<div class="mood-serene">{mood}</div>', unsafe_allow_html=True)

    # Breathing guide
    st.markdown('<div class="breath-guide">', unsafe_allow_html=True)
    st.markdown('<div class="breath-circle"></div>', unsafe_allow_html=True)
    st.markdown('<div class="breath-text">🫁 Breathe In... → 💨 Out... → 😌 Rest</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Disclaimer
    st.markdown(
        '<div style="text-align:center; color:#94a3b8; font-size:0.92rem; margin:2.5rem 0; line-height:1.6;">'
        '🛡️ Unsaid provides emotional support only and does not offer medical advice or diagnosis.'
        '</div>',
        unsafe_allow_html=True
    )

    # Trusted contact
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

    st.markdown('</div>', unsafe_allow_html=True)  # sanctuary-glass

    # Footer
    st.markdown(
        '<div style="text-align:center; color:#64748b; font-size:0.85rem; margin-top:3rem; padding-top:2rem; border-top:1px solid rgba(71,71,99,0.3);">'
        '💾 Everything stays private on your device'
        '</div>',
        unsafe_allow_html=True
    )
