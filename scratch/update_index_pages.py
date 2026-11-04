import re

# Read current index.html
with open(r"d:\project\porto26\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add CSS for .card-thumb if not already present
thumb_css = """
  /* Card Image Thumbnails */
  .card-thumb {
    width: 100%;
    height: 180px;
    background: #0d0d0d;
    border: 1px solid var(--divider);
    overflow: hidden;
    margin-bottom: 14px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .card.featured-card .card-thumb {
    height: 230px;
  }
  .card-thumb img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform .35s ease, filter .35s ease;
    filter: brightness(0.92) contrast(1.05);
  }
  .card:hover .card-thumb img {
    transform: scale(1.04);
    filter: brightness(1.05) contrast(1.1);
  }
"""

if ".card-thumb" not in content:
    # insert right after .card{ ... }
    content = content.replace(".card{", thumb_css + "\n  .card{", 1)

# 2. Build the updated HTML for the PROJECTS section
projects_section_html = """<!-- PROJECTS -->
<section id="projects" data-num="05">
  <div class="side-label">05 / Build Log</div>
  <div class="wrap">
    <div class="sec-head fade-in">
      <span class="sec-num">05</span>
      <span class="sec-kicker">Projects / Engineering Build Log</span>
      <span class="sec-rule"></span>
    </div>

    <div class="filters fade-in" id="filters">
      <button class="filter active" data-filter="all">All</button>
      <button class="filter" data-filter="drone">Drone / Control</button>
      <button class="filter" data-filter="embedded">Embedded / Firmware</button>
      <button class="filter" data-filter="pcb">PCB / Hardware</button>
      <button class="filter" data-filter="fpga">FPGA / Digital</button>
      <button class="filter" data-filter="iiot">IIoT / HMI</button>
    </div>

    <!-- FEATURED FLAGSHIP CARDS -->
    <div class="featured">
      <a class="card featured-card fade-in" href="projects/oil-palm-drone.html" data-cats="drone embedded software">
        <div class="card-thumb">
          <img src="uploads/projects/drone-prototype-assembly.jpg" alt="Autonomous Oil Palm Drone" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">01 / FLAGSHIP</span>
          <span class="card-badge research">UAV &middot; Jetson &middot; Vision</span>
        </div>
        <h3><span class="glyph">&#x25B2;</span>Autonomous Oil Palm Pollination Drone</h3>
        <p>End-to-end autonomous UAV for precision agriculture. Deterministic flight control via Pymavlink/MAVSDK, ROS-based digital twin SITL validation, real-time YOLOv11 target detection on Jetson Nano, and an STM32-actuated pneumatic pollen dispersal payload. Modeled in SolidWorks.</p>
        <div class="stack-tags">
          <span class="t">Pixhawk</span><span class="t">Jetson Nano</span><span class="t">ROS</span>
          <span class="t">YOLOv11</span><span class="t">STM32</span><span class="t">MAVSDK</span><span class="t">SolidWorks</span>
        </div>
        <span class="read-link">Read engineering case study &rarr;</span>
      </a>

      <a class="card featured-card fade-in" href="projects/l1-adaptive-control-uav.html" data-cats="drone software">
        <div class="card-thumb">
          <img src="uploads/projects/l1-adaptive-drone-testing.jpg" alt="Adaptive L1 UAV Control" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">02 / THESIS</span>
          <span class="card-badge research">Lyapunov &middot; STM32F407 &middot; HIL</span>
        </div>
        <h3><span class="glyph">&#x25B2;</span>HIL Testing Adaptive L1 Control for UAV Heavy Payload Drop on STM32F407 (Pixhawk)</h3>
        <p>Proven via Lyapunov stability and validated in hard real-time Hardware-in-the-Loop (HIL) on an STM32F407 Pixhawk flight controller. Rejects abrupt 40% mass shedding with &lt;0.8s settling time and &lt;3&deg; attitude error without motor desynchronization.</p>
        <div class="stack-tags">
          <span class="t">STM32F407</span><span class="t">Pixhawk</span><span class="t">MATLAB</span>
          <span class="t">ROS</span><span class="t">Gazebo</span><span class="t">HIL / SITL</span><span class="t">C++</span>
        </div>
        <span class="read-link">Read engineering case study &rarr;</span>
      </a>

      <a class="card featured-card fade-in" href="projects/pcb-reflow-conveyor-cv-sorting.html" data-cats="embedded pcb software">
        <div class="card-thumb">
          <img src="uploads/projects/reflow-oven-bench-setup.png" alt="PCB Reflow Conveyor CV Sorting" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">03 / FLAGSHIP</span>
          <span class="card-badge research">STM32 &middot; FreeRTOS &middot; CV</span>
        </div>
        <h3><span class="glyph">&#x25B2;</span>PCB Reflow Heating Conveyor System with CV Defect Sorting</h3>
        <p>Industrial reflow oven prototype with automated conveyor mechatronics. STM32F103 firmware on FreeRTOS with 6 static tasks, watchdog supervisor, 250ms closed-loop PID thermal profiling (&plusmn;2&deg;C precision), and Raspberry Pi optical inspection with servo defect sorting.</p>
        <div class="stack-tags">
          <span class="t">STM32F103</span><span class="t">FreeRTOS</span><span class="t">Raspberry Pi</span>
          <span class="t">OpenCV</span><span class="t">PID Thermal</span><span class="t">SolidWorks</span>
        </div>
        <span class="read-link">Read engineering case study &rarr;</span>
      </a>

      <a class="card featured-card fade-in" href="projects/mipi-bridge-board.html" data-cats="pcb hardware">
        <div class="card-thumb">
          <img src="uploads/projects/mipi-bridge-3d.png" alt="MIPI DSI to HDMI Bridge Board" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">04 / HIGH-SPEED PCB</span>
          <span class="card-badge research">4-Layer &middot; 90&Omega; Diff &middot; LT8912B</span>
        </div>
        <h3><span class="glyph">&#x25B2;</span>MIPI DSI to HDMI/LVDS Bridge Board for ESP32-P4</h3>
        <p>High-speed 4-layer PCB (45 &times; 65 mm) centered on the LT8912B bridge IC. Controlled 90&Omega; differential impedance routing for MIPI DSI and HDMI TMDS pairs, JLC04161H stackup, 1.8V/3.3V/5V power tree with pi-filters, 9x LBSS138 level shifters, and RClamp0524P ESD protection.</p>
        <div class="stack-tags">
          <span class="t">KiCad</span><span class="t">LT8912B</span><span class="t">ESP32-P4</span>
          <span class="t">4-Layer PCB</span><span class="t">90&Omega; Diff</span><span class="t">ESD</span>
        </div>
        <span class="read-link">Read engineering case study &rarr;</span>
      </a>

      <a class="card featured-card fade-in" href="projects/fpga-cnn-eye-state.html" data-cats="fpga hardware software">
        <div class="card-thumb">
          <img src="uploads/projects/fpga-cnn-block-diagram.png" alt="FPGA CNN Accelerator" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">05 / FPGA DIGITAL DESIGN</span>
          <span class="card-badge research">Artix-7 &middot; Verilog &middot; INT8</span>
        </div>
        <h3><span class="glyph">&#x25B2;</span>Basys 3 FPGA CNN Eye-State Classifier (Artix-7)</h3>
        <p>Bit-exact hardware accelerator for an INT8 quantized Convolutional Neural Network on Xilinx Artix-7 (Basys 3). Achieves 98.1% accuracy and 100% bit-exact match against PyTorch golden model with a pipelined single-MAC datapath consuming 0 DSP blocks (pure LUT/FF logic).</p>
        <div class="stack-tags">
          <span class="t">Verilog HDL</span><span class="t">Artix-7</span><span class="t">Vivado</span>
          <span class="t">INT8 Quant</span><span class="t">PyTorch</span><span class="t">0 DSP</span>
        </div>
        <span class="read-link">Read engineering case study &rarr;</span>
      </a>
    </div>

    <!-- REGULAR GRID CARDS -->
    <div class="proj-grid">
      <a class="card fade-in" href="projects/atmega128-dev-board.html" data-cats="pcb embedded hardware">
        <div class="card-thumb">
          <img src="uploads/projects/atmega128-dev-board-3d.png" alt="ATmega128 Dev Board" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">06</span>
          <span class="card-badge">Hardware</span>
        </div>
        <h3><span class="glyph">&#x25C6;</span>ATmega128 Development Board</h3>
        <p>Pocket-sized 60 &times; 35 mm 2-layer MCU board. USB Type-C sink with 5.1k&Omega; pulldowns, isolated 10&micro;H LC analog filter for 10-bit ADC stability, CH340C DTR auto-reset, and length-matched 90&Omega; USB differential pairs.</p>
        <div class="stack-tags">
          <span class="t">KiCad</span><span class="t">ATmega128</span><span class="t">Type-C</span><span class="t">LC Filter</span>
        </div>
        <span class="read-link">Read case study &rarr;</span>
      </a>

      <a class="card fade-in" href="projects/industrial-pid-delivery-box.html" data-cats="embedded iiot software">
        <div class="card-thumb">
          <img src="uploads/projects/delivery-box-closed.gif" alt="Control Temperature Food Delivery Box" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">07</span>
          <span class="card-badge">IoT &middot; RTOS</span>
        </div>
        <h3><span class="glyph">&#x25C6;</span>Control Temperature Food Delivery Box</h3>
        <p>Dual-core ESP32 with FreeRTOS. Core 0 runs dual PID thermal loops holding 23&deg;C (TEC Peltier) and 45&deg;C (PTC heater); Core 1 streams live telemetry to a custom mobile app. Custom PDB with INA219, BMS, and MOSFET drivers.</p>
        <div class="stack-tags">
          <span class="t">ESP32</span><span class="t">FreeRTOS</span><span class="t">PID</span><span class="t">Peltier</span><span class="t">PDB</span>
        </div>
        <span class="read-link">Read case study &rarr;</span>
      </a>

      <a class="card fade-in" href="projects/automotive-sensor-wire-harness.html" data-cats="hardware">
        <div class="card-thumb">
          <img src="uploads/projects/wire-harness-top.jpg" alt="Automotive Sensor Wire Harness" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">08</span>
          <span class="card-badge">Automotive R&amp;D</span>
        </div>
        <h3><span class="glyph">&#x25C6;</span>Automotive Sensor Wire Harness</h3>
        <p>PT Hana Master Jaya R&amp;D internship. Rev. 0 prototype harness: 3-leg T-geometry linking 8-pin, 3-pin, and dual 2-pin sealed automotive connectors with 15 circuits. Prepared complete drawings, BOM, and JIS C 2805 crimp pull specs.</p>
        <div class="stack-tags">
          <span class="t">Wire Harness</span><span class="t">AutoCAD</span><span class="t">BOM</span><span class="t">JIS C 2805</span>
        </div>
        <span class="read-link">Read case study &rarr;</span>
      </a>

      <a class="card fade-in" href="projects/fan-speed-controller.html" data-cats="pcb embedded hardware">
        <div class="card-thumb">
          <img src="uploads/projects/fan-controller-board-top.jpg" alt="CH32V003 Fan Speed Controller" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">09</span>
          <span class="card-badge">RISC-V &middot; Hardware</span>
        </div>
        <h3><span class="glyph">&#x25C6;</span>CH32V003 RISC-V Fan Speed Controller</h3>
        <p>Cost-effective intelligent cooling fan controller built around the $0.10 CH32V003 RISC-V MCU. 25kHz ultrasonic PWM generation, closed-loop tachometer feedback (&plusmn;20 RPM), PC817 optoisolation, and 1N4007 reverse polarity protection.</p>
        <div class="stack-tags">
          <span class="t">CH32V003</span><span class="t">RISC-V</span><span class="t">PC817</span><span class="t">25kHz PWM</span><span class="t">PID</span>
        </div>
        <span class="read-link">Read case study &rarr;</span>
      </a>

      <a class="card fade-in" href="projects/usbc-boost-module.html" data-cats="pcb hardware">
        <div class="card-thumb">
          <img src="uploads/projects/usbc-boost-3d.gif" alt="USB-C to 12V Boost Module" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">10</span>
          <span class="card-badge">Power Electronics</span>
        </div>
        <h3><span class="glyph">&#x25C6;</span>USB-C to 12V Boost Module (CX8823)</h3>
        <p>High-efficiency step-up DC-DC converter providing 12V 1.5A from 5V USB-C. Sized with a 3.3&micro;H shielded inductor for continuous conduction, 470&micro;F low-ESR bulk filtering (&lt;25mV ripple), TVS hot-plug surge clamping, and DNP config pads.</p>
        <div class="stack-tags">
          <span class="t">CX8823</span><span class="t">Boost DC-DC</span><span class="t">TVS Protection</span><span class="t">KiCad</span>
        </div>
        <span class="read-link">Read case study &rarr;</span>
      </a>

      <a class="card fade-in" href="projects/custom-stm32-pcb.html" data-cats="pcb embedded hardware">
        <div class="card-thumb">
          <img src="uploads/projects/mini-stm32-pcb-3d.gif" alt="Custom Mini STM32 PCB" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">11</span>
          <span class="card-badge">MCU Hardware</span>
        </div>
        <h3><span class="glyph">&#x25C6;</span>Custom Mini STM32 PCB Design</h3>
        <p>Minimalist system board for STM32F103C8T6 (ARM Cortex-M3 @ 72MHz). Continuous ground plane, 16MHz crystal load-matched capacitor tank, 22&Omega; USB 2.0 differential trace damping, AMS1117-3.3 rail, and 4-pin SWD debug port.</p>
        <div class="stack-tags">
          <span class="t">STM32F103</span><span class="t">ARM M3</span><span class="t">KiCad</span><span class="t">USB 2.0</span><span class="t">SWD</span>
        </div>
        <span class="read-link">Read case study &rarr;</span>
      </a>

      <a class="card fade-in" href="projects/hourglass-atmega328p-pcb.html" data-cats="pcb embedded hardware">
        <div class="card-thumb">
          <img src="uploads/projects/hourglass-schematic.gif" alt="Hourglass PCB" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">12</span>
          <span class="card-badge">Novelty Hardware</span>
        </div>
        <h3><span class="glyph">&#x25C6;</span>Custom Hourglass PCB with ATmega8A</h3>
        <p>Two-board stacked sand timer with 29 blue LEDs driven by 4x 74HC595 shift registers in SPI cascade. Dual SW-200D tilt switches detect physical inversion; pushbuttons select 1/5/10 min countdowns with active buzzer alarms and LiPo charging.</p>
        <div class="stack-tags">
          <span class="t">ATmega8A</span><span class="t">74HC595</span><span class="t">SPI</span><span class="t">SW-200D</span><span class="t">TP4056</span>
        </div>
        <span class="read-link">Read case study &rarr;</span>
      </a>

      <a class="card fade-in" href="projects/mini-logic-analyzer.html" data-cats="embedded hardware">
        <div class="card-thumb">
          <img src="uploads/projects/bridge-faulty-sensor.gif" alt="Mini Logic Analyzer" loading="lazy" />
        </div>
        <div class="card-top">
          <span class="card-num">13</span>
          <span class="card-badge">Instrumentation</span>
        </div>
        <h3><span class="glyph">&#x25C6;</span>Mini Logic Analyzer (8-Ch 24MHz DMA DAQ)</h3>
        <p>Low-cost 8-channel logic analyzer built on STM32 ARM Cortex-M4. Hardware timer triggered DMA acquisition at 24MHz parallel sampling with double-buffered circular SRAM streaming over USB VCP. Compatible with open-source Sigrok / PulseView.</p>
        <div class="stack-tags">
          <span class="t">STM32F4</span><span class="t">DMA</span><span class="t">24MHz DAQ</span><span class="t">Sigrok</span><span class="t">PulseView</span>
        </div>
        <span class="read-link">Read case study &rarr;</span>
      </a>
    </div>

    <!-- COLLAPSIBLE MORE PROJECTS LIST -->
    <div class="view-all fade-in">
      <button class="btn" id="moreBtn">View All Projects (18) <span class="arr" id="moreArr">&darr;</span></button>
      <div class="extra-line"></div>
    </div>

    <div class="more-list" id="moreList">
      <ul>
        <li><a href="projects/sap-flow-sensor.html" class="more-item-link"><span class="idx">14</span><span class="name">Plant Sap Flow Sensor (Low-Noise Thermocouple Front-End &amp; Granier Method)</span><span class="tools">Analog AFE &middot; Thermocouple &middot; SLA 3D &rarr;</span></a></li>
        <li><a href="projects/soccer-robot-ep-lab.html" class="more-item-link"><span class="idx">15</span><span class="name">Soccer Robot (3-Wheel Holonomic Omni-Drive with Kotlin Android Wi-Fi App)</span><span class="tools">Kotlin &middot; Android &middot; SolidWorks &middot; C++ &rarr;</span></a></li>
        <li><a href="projects/iiot-motor-control-system.html" class="more-item-link"><span class="idx">16</span><span class="name">IIoT Capstone Motor Control &amp; Cloud SCADA (Omron PLC &amp; Weintek HMI)</span><span class="tools">Omron PLC &middot; Node-RED &middot; Next.js &middot; MongoDB &rarr;</span></a></li>
        <li><a href="projects/micro-hydro-hmi-system.html" class="more-item-link"><span class="idx">17</span><span class="name">MicroHydroPower TeleLab &amp; Aeroponic HMI System (ISA-101 SCADA)</span><span class="tools">ISA-101 &middot; FreeRTOS &middot; MQTT &middot; MySQL &rarr;</span></a></li>
        <li><a href="projects/tinyml-motor-anomaly.html" class="more-item-link"><span class="idx">18</span><span class="name">TinyML Machine Vibration Anomaly Detection (512-Point FFT on ESP32-S3)</span><span class="tools">TinyML &middot; 512-FFT &middot; Autoencoder &middot; C++ &rarr;</span></a></li>
      </ul>
    </div>
  </div>
</section>
"""

# Regex replacement of <section id="projects" ... </section>
pattern = re.compile(r'<section id="projects".*?</section>', re.DOTALL)
new_content = pattern.sub(projects_section_html, content)

# Also update categories list in javascript
old_cats_js = "const cats = ['drone','embedded','pcb','iiot','software'];"
new_cats_js = "const cats = ['drone','embedded','pcb','fpga','iiot','software','hardware'];"
if old_cats_js in new_content:
    new_content = new_content.replace(old_cats_js, new_cats_js)

# Write to all 4 target files
files_to_update = [
    r"d:\project\porto26\index.html",
    r"d:\project\porto26\Portfolio.html",
    r"d:\project\porto26\project\index.html",
    r"d:\project\porto26\project\Portfolio.html"
]

for file_path in files_to_update:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated: {file_path}")

print("All index and portfolio pages updated successfully!")

