import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="GlobalInternet.py | 3D Promo",
    page_icon="🌍",
    layout="wide"
)

# ---------- SIDEBAR with spinning globe ----------
with st.sidebar:
    st.markdown("""
    <style>
    .spin-logo {
        font-size: 60px;
        animation: spin 4s linear infinite;
        display: inline-block;
    }
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    </style>
    <div style="text-align: center;">
        <div class="spin-logo">🌍</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("## **GlobalInternet.py**")
    st.markdown("---")
    st.markdown("**Built by Gesner Deslandes** – Coder in Chief")
    st.markdown("📞 (509)-47385663")
    st.markdown("✉️ deslandes78@gmail.com")
    st.markdown("---")
    st.markdown("### 🚀 Welcome to the future of software")
    st.info("Click the button below to hear an AI voice promote our website.")

# ---------- MAIN AREA: 3D Globe with orbiting text ----------
st.markdown("<h1 style='text-align: center;'>🌐 GlobalInternet.py – Software on Demand</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Watch the globe spin with our message – then click the button to hear an AI voice.</p>", unsafe_allow_html=True)

# HTML/JS component that creates the 3D scene
globe_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; }
        #controls {
            position: absolute;
            bottom: 20px;
            left: 20px;
            z-index: 100;
            background: rgba(0,0,0,0.6);
            padding: 10px 20px;
            border-radius: 30px;
            color: white;
            pointer-events: none;
        }
        #speakBtn {
            position: absolute;
            bottom: 20px;
            right: 20px;
            z-index: 100;
            background: #ff6b6b;
            border: none;
            color: white;
            font-weight: bold;
            padding: 12px 24px;
            border-radius: 40px;
            cursor: pointer;
            font-size: 16px;
            transition: 0.2s;
            pointer-events: auto;
        }
        #speakBtn:hover {
            background: #ff4b4b;
            transform: scale(1.02);
        }
    </style>
</head>
<body>
    <div id="controls">🌍 Spinning globe + orbiting text | Drag to rotate</div>
    <button id="speakBtn">🔊 AI Voice – Promote Website</button>

    <script type="importmap">
        {
            "imports": {
                "three": "https://unpkg.com/three@0.128.0/build/three.module.js",
                "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/"
            }
        }
    </script>

    <script type="module">
        import * as THREE from 'three';
        import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
        import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';

        // --- setup scene
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x050b1a);
        scene.fog = new THREE.FogExp2(0x050b1a, 0.005);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(0, 1, 3.5);
        camera.lookAt(0, 0, 0);

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.shadowMap.enabled = true;
        document.body.appendChild(renderer.domElement);

        // CSS2 renderer for text
        const labelRenderer = new CSS2DRenderer();
        labelRenderer.setSize(window.innerWidth, window.innerHeight);
        labelRenderer.domElement.style.position = 'absolute';
        labelRenderer.domElement.style.top = '0px';
        labelRenderer.domElement.style.left = '0px';
        labelRenderer.domElement.style.pointerEvents = 'none';
        document.body.appendChild(labelRenderer.domElement);

        // --- controls (allow user to drag, but auto-rotate by default)
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.autoRotate = true;
        controls.autoRotateSpeed = 1.5;
        controls.enableZoom = true;
        controls.enablePan = true;
        controls.target.set(0, 0, 0);

        // --- lighting
        const ambient = new THREE.AmbientLight(0x404060);
        scene.add(ambient);
        const dirLight = new THREE.DirectionalLight(0xffffff, 1);
        dirLight.position.set(5, 10, 7);
        dirLight.castShadow = true;
        scene.add(dirLight);
        const fillLight = new THREE.PointLight(0x88aaff, 0.3);
        fillLight.position.set(1, 1, 2);
        scene.add(fillLight);
        const backLight = new THREE.PointLight(0xffaa66, 0.2);
        backLight.position.set(-1, 0, -2);
        scene.add(backLight);

        // --- earth texture
        const earthGeometry = new THREE.SphereGeometry(1, 64, 64);
        const textureLoader = new THREE.TextureLoader();
        const earthTexture = textureLoader.load('https://threejs.org/examples/textures/planets/earth_atmos_2048.jpg');
        const earthMaterial = new THREE.MeshStandardMaterial({ map: earthTexture, roughness: 0.5, metalness: 0.1 });
        const earth = new THREE.Mesh(earthGeometry, earthMaterial);
        earth.castShadow = true;
        earth.receiveShadow = true;
        scene.add(earth);

        // --- orbiting text (CSS2D)
        const messages = [
            "🌐 GlobalInternet.py",
            "🐍 Python on Demand",
            "🚀 AI & Web Apps",
            "🌍 Worldwide Clients",
            "💡 Build → Ship → Own",
            "📧 deslandes78@gmail.com"
        ];
        const orbitRadius = 1.6;
        const textObjects = [];
        
        messages.forEach((msg, idx) => {
            const div = document.createElement('div');
            div.textContent = msg;
            div.style.color = '#ffdd99';
            div.style.fontSize = '20px';
            div.style.fontWeight = 'bold';
            div.style.background = 'rgba(0,0,0,0.6)';
            div.style.padding = '6px 14px';
            div.style.borderRadius = '30px';
            div.style.border = '1px solid #ffaa66';
            div.style.whiteSpace = 'nowrap';
            div.style.fontFamily = 'Arial';
            const label = new CSS2DObject(div);
            // Position around the equator, evenly spaced
            const angle = (idx / messages.length) * Math.PI * 2;
            label.position.x = Math.cos(angle) * orbitRadius;
            label.position.z = Math.sin(angle) * orbitRadius;
            label.position.y = 0.2 * Math.sin(angle * 2); // slight vertical wave
            scene.add(label);
            textObjects.push({ label, angle, speed: 0.005, radius: orbitRadius });
        });

        // Animation loop to rotate the text around the globe
        function animate() {
            requestAnimationFrame(animate);
            // rotate text objects around Y axis
            textObjects.forEach(obj => {
                obj.angle += obj.speed;
                obj.label.position.x = Math.cos(obj.angle) * obj.radius;
                obj.label.position.z = Math.sin(obj.angle) * obj.radius;
                obj.label.position.y = 0.2 * Math.sin(obj.angle * 2);
            });
            controls.update(); // updates auto-rotate and damping
            renderer.render(scene, camera);
            labelRenderer.render(scene, camera);
        }
        animate();

        // --- resize handler
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
            labelRenderer.setSize(window.innerWidth, window.innerHeight);
        });

        // --- AI voice button (Web Speech API)
        const speakBtn = document.getElementById('speakBtn');
        speakBtn.addEventListener('click', () => {
            const speech = new SpeechSynthesisUtterance();
            speech.text = "Welcome to GlobalInternet dot py. Your best choice for Python software on demand. Visit our website today to turn your ideas into reality. Built by Gesner Deslandes.";
            speech.lang = 'en-US';
            speech.rate = 0.9;
            speech.pitch = 1.0;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(speech);
        });
    </script>
</body>
</html>
"""

st.components.v1.html(globe_html, height=700, scrolling=False)

st.markdown("---")
st.caption("Powered by Three.js | Voice by Web Speech API | Globe texture from Three.js examples")
