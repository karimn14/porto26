import os

files_to_update = [
    r"d:\project\porto26\index.html",
    r"d:\project\porto26\Portfolio.html",
    r"d:\project\porto26\project\index.html",
    r"d:\project\porto26\project\Portfolio.html"
]

css_addition = """
  .more-list a.more-item-link {
    display: flex; align-items: baseline; gap: 14px; width: 100%;
    text-decoration: none; color: inherit;
    transition: color .2s ease;
    cursor: none;
  }
  .more-list a.more-item-link:hover .name {
    color: var(--accent);
  }
"""

old_target_block = """    <!-- FEATURED -->
    <div class="featured">
      <a class="card featured-card fade-in" href="projects/oil-palm-drone.html" data-cats="drone embedded software">
        <div class="card-top">
          <span class="card-num">01 / FLAGSHIP</span>
          <span class="card-badge research">Internship · Drone</span>
        </div>
        <h3><span class="glyph">◈</span>Autonomous Oil Palm Pollination Drone</h3>
        <p>End-to-end autonomous drone for precision agriculture. Core flight control via Pymavlink/MAVSDK with ROS as a validation architecture. Digital twin simulation + SITL/HIL testing. Waypoint navigation, real-time YOLOv11 obstacle avoidance (custom model), STM32 payload actuation, FastAPI web telemetry dashboard. Mechanical design in SolidWorks.</p>
        <div class="stack-tags">
          <span class="t">Pixhawk</span><span class="t">Jetson Nano</span><span class="t">ROS</span>
          <span class="t">YOLOv11</span><span class="t">STM32</span><span class="t">FastAPI</span>
          <span class="t">MAVSDK</span><span class="t">SolidWorks</span>
        </div>
        <span class="read-link">Read case study →</span>
      </a>

      <div class="card featured-card fade-in" data-cats="drone software">
        <div class="card-top">
          <span class="card-num">02 / THESIS</span>
          <span class="card-badge research">Research</span>
        </div>
        <h3><span class="glyph">◈</span>MPC + LESO + ETC Robust Control for UAV Payload Drop</h3>
        <p>Comparative analysis of robust control for sudden mass shedding on a quadrotor. MIMO MPC augmented with a Linear Extended State Observer and Event-Triggered Control. HIL testing on Pixhawk 2.4.8. Significant reduction in recovery time vs. baseline PID.</p>
        <div class="stack-tags">
          <span class="t">MATLAB</span><span class="t">C++</span><span class="t">ArduPilot</span>
          <span class="t">Pixhawk</span><span class="t">ROS</span><span class="t">Gazebo</span>
          <span class="t">SITL / HIL</span>
        </div>
      </div>
    </div>

    <!-- REGULAR -->
    <div class="proj-grid">
      <div class="card fade-in" data-cats="embedded software">
        <div class="card-top">
          <span class="card-num">03</span>
          <span class="card-badge">Personal</span>
        </div>
        <h3><span class="glyph">▸</span>TinyML Motor Anomaly Detection</h3>
        <p>Autoencoder NN deployed on ESP32-S3 for vibration-based bearing fault detection. Frequency-domain analysis, high-accuracy anomaly classification with minimal bandwidth.</p>
        <div class="stack-tags">
          <span class="t">TinyML</span><span class="t">Python</span><span class="t">C++</span><span class="t">ESP32-S3</span>
        </div>
      </div>

      <div class="card fade-in" data-cats="embedded iiot">
        <div class="card-top">
          <span class="card-num">04</span>
          <span class="card-badge">Personal</span>
        </div>
        <h3><span class="glyph">▸</span>Industrial PID Temperature Food Delivery Box</h3>
        <p>Dual-core ESP32 + RTOS. PID control: 23°C (TEC Peltier) + 45°C (PTC heater). Hardware watchdog, solar charging, self-hosted web server, mobile app (Kodular).</p>
        <div class="stack-tags">
          <span class="t">ESP32</span><span class="t">C++ / Arduino</span><span class="t">RTOS</span><span class="t">IoT</span><span class="t">PID</span>
        </div>
      </div>

      <div class="card fade-in" data-cats="pcb embedded">
        <div class="card-top">
          <span class="card-num">05</span>
          <span class="card-badge">Personal</span>
        </div>
        <h3><span class="glyph">▸</span>Custom Mini STM32 PCB (STM32F103C8T6)</h3>
        <p>Full design lifecycle in KiCad: schematic → 2-layer layout. AMS1117 LDO, 16 MHz crystal with load capacitance calc, USB 2.0 differential pairs, SWD debug, ground plane, Gerber output.</p>
        <div class="stack-tags">
          <span class="t">KiCad</span><span class="t">STM32F103</span><span class="t">PCB Design</span><span class="t">EMC</span>
        </div>
      </div>

      <div class="card fade-in" data-cats="software iiot">
        <div class="card-top">
          <span class="card-num">06</span>
          <span class="card-badge">Internship</span>
        </div>
        <h3><span class="glyph">▸</span>Intelligent EV Charging Station</h3>
        <p>Full-stack CSMS: FastAPI backend, XGBoost demand forecasting with background model updates, ReactJS dashboard with live charts. Raspberry Pi edge node + PN532 RFID + kiosk web panel.</p>
        <div class="stack-tags">
          <span class="t">ReactJS</span><span class="t">FastAPI</span><span class="t">XGBoost</span><span class="t">Raspberry Pi</span><span class="t">MySQL</span><span class="t">RFID</span>
        </div>
      </div>

      <div class="card fade-in" data-cats="iiot software">
        <div class="card-top">
          <span class="card-num">07</span>
          <span class="card-badge">Capstone</span>
        </div>
        <h3><span class="glyph">▸</span>IIoT Capstone — Motor Control System</h3>
        <p>Multi-layer data viz: Node-RED HMI (MQTT + local DB) + NextJS cloud app (MongoDB). HMI Weintek config with Omron PLC via CX Designer.</p>
        <div class="stack-tags">
          <span class="t">Node-RED</span><span class="t">NextJS</span><span class="t">MongoDB</span><span class="t">HMI Weintek</span><span class="t">MQTT</span><span class="t">PLC</span>
        </div>
      </div>

      <div class="card fade-in" data-cats="iiot embedded">
        <div class="card-top">
          <span class="card-num">08</span>
          <span class="card-badge">Capstone</span>
        </div>
        <h3><span class="glyph">▸</span>Micro HydroPower HMI Learning System</h3>
        <p>Industrial HMI from scratch: login, role-based settings, control, data management. ISA101 + ISO 11064-5 standards. MQTT + MySQL + RTOS real-time data acquisition.</p>
        <div class="stack-tags">
          <span class="t">Node-RED</span><span class="t">MQTT</span><span class="t">MySQL</span><span class="t">RTOS</span><span class="t">ISA101</span>
        </div>
      </div>

      <div class="card fade-in" data-cats="embedded pcb">
        <div class="card-top">
          <span class="card-num">09</span>
          <span class="card-badge">Personal</span>
        </div>
        <h3><span class="glyph">▸</span>SAP Flow Sensor</h3>
        <p>Compact plant health monitoring: analog thermocouple amplification circuit, microcontroller DAQ, custom data acquisition formula, 3D-printed enclosure.</p>
        <div class="stack-tags">
          <span class="t">Analog Circuit</span><span class="t">Thermocouple</span><span class="t">3D Design</span>
        </div>
      </div>

      <div class="card fade-in" data-cats="embedded software">
        <div class="card-top">
          <span class="card-num">10</span>
          <span class="card-badge">Capstone</span>
        </div>
        <h3><span class="glyph">▸</span>Soccer Robot — Engineering Physics Lab</h3>
        <p>3D-modeled robot with WiFi-connected Android control app (Android Studio / Kotlin). Led system integration. Arduino firmware for motor + control logic.</p>
        <div class="stack-tags">
          <span class="t">Arduino</span><span class="t">C++</span><span class="t">Android Studio</span><span class="t">Kotlin</span><span class="t">SolidWorks</span>
        </div>
      </div>
    </div>

    <div class="view-all fade-in">
      <button class="btn" id="moreBtn">View All Projects <span class="arr" id="moreArr">↓</span></button>
      <div class="extra-line"></div>
    </div>

    <div class="more-list" id="moreList">
      <ul>
        <li><span class="idx">11</span><span class="name">GIC Power System Simulation</span><span class="tools">Slack · PSCAD</span></li>
        <li><span class="idx">12</span><span class="name">Batik Coagulant Modular Processing Unit</span><span class="tools">SolidWorks</span></li>
        <li><span class="idx">13</span><span class="name">Bridge Faulty Sensor FFT</span><span class="tools">Python · MATLAB</span></li>
        <li><span class="idx">14</span><span class="name">FunBox Controller</span><span class="tools">IoT · ESP32</span></li>
        <li><span class="idx">15</span><span class="name">Humanoid Robot Dance</span><span class="tools">C# · 3D CAD</span></li>
        <li><span class="idx">16</span><span class="name">Free Healthy Meal Webapp</span><span class="tools">VueJS · Web2py</span></li>
        <li><span class="idx">17</span><span class="name">Company Landing Pages</span><span class="tools">WordPress</span></li>
        <li><span class="idx">18</span><span class="name">Wind Turbine 3D Model</span><span class="tools">SolidWorks</span></li>
      </ul>
    </div>"""

new_replacement_block = """    <!-- FEATURED -->
    <div class="featured">
      <a class="card featured-card fade-in" href="projects/oil-palm-drone.html" data-cats="drone embedded software">
        <div class="card-top">
          <span class="card-num">01 / FLAGSHIP</span>
          <span class="card-badge research">Internship · Drone</span>
        </div>
        <h3><span class="glyph">◈</span>Autonomous Oil Palm Pollination Drone</h3>
        <p>End-to-end autonomous drone for precision agriculture. Core flight control via Pymavlink/MAVSDK with ROS as a validation architecture. Digital twin simulation + SITL/HIL testing. Waypoint navigation, real-time YOLOv11 obstacle avoidance (custom model), STM32 payload actuation, FastAPI web telemetry dashboard. Mechanical design in SolidWorks.</p>
        <div class="stack-tags">
          <span class="t">Pixhawk</span><span class="t">Jetson Nano</span><span class="t">ROS</span>
          <span class="t">YOLOv11</span><span class="t">STM32</span><span class="t">FastAPI</span>
          <span class="t">MAVSDK</span><span class="t">SolidWorks</span>
        </div>
        <span class="read-link">Read case study →</span>
      </a>

      <a class="card featured-card fade-in" href="projects/mpc-leso-etc-quadrotor.html" data-cats="drone software">
        <div class="card-top">
          <span class="card-num">02 / THESIS</span>
          <span class="card-badge research">Research</span>
        </div>
        <h3><span class="glyph">◈</span>MPC + LESO + ETC Robust Control for UAV Payload Drop</h3>
        <p>Comparative analysis of robust control for sudden mass shedding on a quadrotor. MIMO MPC augmented with a Linear Extended State Observer and Event-Triggered Control. HIL testing on Pixhawk 2.4.8. Significant reduction in recovery time vs. baseline PID.</p>
        <div class="stack-tags">
          <span class="t">MATLAB</span><span class="t">C++</span><span class="t">ArduPilot</span>
          <span class="t">Pixhawk</span><span class="t">ROS</span><span class="t">Gazebo</span>
          <span class="t">SITL / HIL</span>
        </div>
        <span class="read-link">Read case study →</span>
      </a>
    </div>

    <!-- REGULAR -->
    <div class="proj-grid">
      <a class="card fade-in" href="projects/tinyml-motor-anomaly.html" data-cats="embedded software">
        <div class="card-top">
          <span class="card-num">03</span>
          <span class="card-badge">Personal</span>
        </div>
        <h3><span class="glyph">▸</span>TinyML Motor Anomaly Detection</h3>
        <p>Autoencoder NN deployed on ESP32-S3 for vibration-based bearing fault detection. Frequency-domain analysis, high-accuracy anomaly classification with minimal bandwidth.</p>
        <div class="stack-tags">
          <span class="t">TinyML</span><span class="t">Python</span><span class="t">C++</span><span class="t">ESP32-S3</span>
        </div>
        <span class="read-link">Read case study →</span>
      </a>

      <a class="card fade-in" href="projects/industrial-pid-delivery-box.html" data-cats="embedded iiot">
        <div class="card-top">
          <span class="card-num">04</span>
          <span class="card-badge">Personal</span>
        </div>
        <h3><span class="glyph">▸</span>Industrial PID Temperature Food Delivery Box</h3>
        <p>Dual-core ESP32 + RTOS. PID control: 23°C (TEC Peltier) + 45°C (PTC heater). Hardware watchdog, solar charging, self-hosted web server, mobile app (Kodular).</p>
        <div class="stack-tags">
          <span class="t">ESP32</span><span class="t">C++ / Arduino</span><span class="t">RTOS</span><span class="t">IoT</span><span class="t">PID</span>
        </div>
        <span class="read-link">Read case study →</span>
      </a>

      <a class="card fade-in" href="projects/custom-stm32-pcb.html" data-cats="pcb embedded">
        <div class="card-top">
          <span class="card-num">05</span>
          <span class="card-badge">Personal</span>
        </div>
        <h3><span class="glyph">▸</span>Custom Mini STM32 PCB (STM32F103C8T6)</h3>
        <p>Full design lifecycle in KiCad: schematic → 2-layer layout. AMS1117 LDO, 16 MHz crystal with load capacitance calc, USB 2.0 differential pairs, SWD debug, ground plane, Gerber output.</p>
        <div class="stack-tags">
          <span class="t">KiCad</span><span class="t">STM32F103</span><span class="t">PCB Design</span><span class="t">EMC</span>
        </div>
        <span class="read-link">Read case study →</span>
      </a>

      <a class="card fade-in" href="projects/intelligent-ev-charging-station.html" data-cats="software iiot">
        <div class="card-top">
          <span class="card-num">06</span>
          <span class="card-badge">Internship</span>
        </div>
        <h3><span class="glyph">▸</span>Intelligent EV Charging Station</h3>
        <p>Full-stack CSMS: FastAPI backend, XGBoost demand forecasting with background model updates, ReactJS dashboard with live charts. Raspberry Pi edge node + PN532 RFID + kiosk web panel.</p>
        <div class="stack-tags">
          <span class="t">ReactJS</span><span class="t">FastAPI</span><span class="t">XGBoost</span><span class="t">Raspberry Pi</span><span class="t">MySQL</span><span class="t">RFID</span>
        </div>
        <span class="read-link">Read case study →</span>
      </a>

      <a class="card fade-in" href="projects/iiot-motor-control-system.html" data-cats="iiot software">
        <div class="card-top">
          <span class="card-num">07</span>
          <span class="card-badge">Capstone</span>
        </div>
        <h3><span class="glyph">▸</span>IIoT Capstone — Motor Control System</h3>
        <p>Multi-layer data viz: Node-RED HMI (MQTT + local DB) + NextJS cloud app (MongoDB). HMI Weintek config with Omron PLC via CX Designer.</p>
        <div class="stack-tags">
          <span class="t">Node-RED</span><span class="t">NextJS</span><span class="t">MongoDB</span><span class="t">HMI Weintek</span><span class="t">MQTT</span><span class="t">PLC</span>
        </div>
        <span class="read-link">Read case study →</span>
      </a>

      <a class="card fade-in" href="projects/micro-hydro-hmi-system.html" data-cats="iiot embedded">
        <div class="card-top">
          <span class="card-num">08</span>
          <span class="card-badge">Capstone</span>
        </div>
        <h3><span class="glyph">▸</span>Micro HydroPower HMI Learning System</h3>
        <p>Industrial HMI from scratch: login, role-based settings, control, data management. ISA101 + ISO 11064-5 standards. MQTT + MySQL + RTOS real-time data acquisition.</p>
        <div class="stack-tags">
          <span class="t">Node-RED</span><span class="t">MQTT</span><span class="t">MySQL</span><span class="t">RTOS</span><span class="t">ISA101</span>
        </div>
        <span class="read-link">Read case study →</span>
      </a>

      <a class="card fade-in" href="projects/sap-flow-sensor.html" data-cats="embedded pcb">
        <div class="card-top">
          <span class="card-num">09</span>
          <span class="card-badge">Personal</span>
        </div>
        <h3><span class="glyph">▸</span>SAP Flow Sensor</h3>
        <p>Compact plant health monitoring: analog thermocouple amplification circuit, microcontroller DAQ, custom data acquisition formula, 3D-printed enclosure.</p>
        <div class="stack-tags">
          <span class="t">Analog Circuit</span><span class="t">Thermocouple</span><span class="t">3D Design</span>
        </div>
        <span class="read-link">Read case study →</span>
      </a>

      <a class="card fade-in" href="projects/soccer-robot-ep-lab.html" data-cats="embedded software">
        <div class="card-top">
          <span class="card-num">10</span>
          <span class="card-badge">Capstone</span>
        </div>
        <h3><span class="glyph">▸</span>Soccer Robot — Engineering Physics Lab</h3>
        <p>3D-modeled robot with WiFi-connected Android control app (Android Studio / Kotlin). Led system integration. Arduino firmware for motor + control logic.</p>
        <div class="stack-tags">
          <span class="t">Arduino</span><span class="t">C++</span><span class="t">Android Studio</span><span class="t">Kotlin</span><span class="t">SolidWorks</span>
        </div>
        <span class="read-link">Read case study →</span>
      </a>
    </div>

    <div class="view-all fade-in">
      <button class="btn" id="moreBtn">View All Projects <span class="arr" id="moreArr">↓</span></button>
      <div class="extra-line"></div>
    </div>

    <div class="more-list" id="moreList">
      <ul>
        <li><a href="projects/gic-power-system.html" class="more-item-link"><span class="idx">11</span><span class="name">GIC Power System Simulation</span><span class="tools">Slack · PSCAD ↗</span></a></li>
        <li><a href="projects/batik-coagulant-unit.html" class="more-item-link"><span class="idx">12</span><span class="name">Batik Coagulant Modular Processing Unit</span><span class="tools">SolidWorks ↗</span></a></li>
        <li><a href="projects/bridge-faulty-sensor-fft.html" class="more-item-link"><span class="idx">13</span><span class="name">Bridge Faulty Sensor FFT</span><span class="tools">Python · MATLAB ↗</span></a></li>
        <li><a href="projects/funbox-controller.html" class="more-item-link"><span class="idx">14</span><span class="name">FunBox Controller</span><span class="tools">IoT · ESP32 ↗</span></a></li>
        <li><a href="projects/humanoid-robot-dance.html" class="more-item-link"><span class="idx">15</span><span class="name">Humanoid Robot Dance</span><span class="tools">C# · 3D CAD ↗</span></a></li>
        <li><a href="projects/free-healthy-meal-webapp.html" class="more-item-link"><span class="idx">16</span><span class="name">Free Healthy Meal Webapp</span><span class="tools">VueJS · Web2py ↗</span></a></li>
        <li><a href="projects/company-landing-pages.html" class="more-item-link"><span class="idx">17</span><span class="name">Company Landing Pages</span><span class="tools">WordPress ↗</span></a></li>
        <li><a href="projects/wind-turbine-3d-model.html" class="more-item-link"><span class="idx">18</span><span class="name">Wind Turbine 3D Model</span><span class="tools">SolidWorks ↗</span></a></li>
      </ul>
    </div>"""

# Normalize endline variations
old_target_block_norm = old_target_block.replace("\r\n", "\n")

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().replace("\r\n", "\n")
        
    if ".more-item-link" not in content:
        content = content.replace("</style>", css_addition + "\n</style>")
        
    if old_target_block_norm in content:
        content = content.replace(old_target_block_norm, new_replacement_block)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully updated {filepath}")
    else:
        print(f"Block match failed in {filepath}")

print("Updater finished.")
