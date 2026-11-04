import os
import sys
import re

print("Starting complete portfolio generator...")

# 18 curated high-value engineering projects
PROJECTS = [
    {
        "slug": "oil-palm-drone",
        "num": "01",
        "badge": "FLAGSHIP / AUTONOMOUS UAV",
        "cat_str": "drone embedded software",
        "title": "Autonomous Oil Palm Pollination Drone",
        "subtitle": "End-to-End Autonomous UAV for Precision Agriculture with Real-Time YOLOv11 Computer Vision, Digital Twin, and STM32 Payload Actuation",
        "role": "Lead Robotics & Embedded Systems Engineer",
        "client": "Autonomous Agri-Tech / ITB",
        "period": "2025 – 2026",
        "stack": ["Pixhawk", "Jetson Nano", "ROS", "YOLOv11", "STM32", "Pymavlink", "MAVSDK", "SolidWorks"],
        "metrics": [
            ("< 50ms", "Actuation Latency"),
            ("30 FPS", "On-Device Inference"),
            ("100%", "Waypoint Precision"),
            ("4-DOF", "Custom Airframe")
        ],
        "summary": "Engineered an end-to-end autonomous quadrotor system for targeted oil palm pollination. Flight control and mission execution are built on Pymavlink and MAVSDK for deterministic low-latency command streaming. A ROS-based digital twin simulates and validates navigation and control algorithms prior to field deployment. Features real-time YOLOv11 vision on Jetson Nano, an STM32-based pneumatic pollen spray actuator, and full-duplex telemetry.",
        "cover_img": "drone-prototype-assembly.jpg",
        "fig1_img": "drone-airframe-3d.gif",
        "fig1_cap": "Figure 1: Custom airframe structural design and modular electronics housing modeled in SolidWorks.",
        "fig2_img": "drone-bench-testing.jpg",
        "fig2_cap": "Figure 2: Ground bench testing and sensor calibration: Pixhawk IMU fusion, Jetson Nano CSI link, and STM32 actuator bus.",
        "gallery_imgs": [
            ("drone-mission-planner.gif", "Mission planner telemetry interface"),
            ("drone-map-view.jpg", "Autonomous GPS waypoint mapping"),
            ("drone-simulation-console.jpg", "ROS digital twin SITL console")
        ],
        "sections": [
            ("overview", "Project Scope & Agronomic Challenge", """
<p>Precision pollination in oil palm plantations presents severe operational constraints: towering canopy heights (8–15 m), erratic tropical gusts, dense leaf clutter, and the demand for milligram-level pollen dosage per flower bunch. Manual pollination is labor-intensive, hazardous, and yields inconsistent fruit bunch set.</p>
<p>To overcome this, I developed an autonomous UAV platform capable of navigating tree rows autonomously, detecting receptive female flower inflorescences in real time, and deploying an electro-pneumatic pollen blast from a stabilized standoff distance of 1.2 meters without human pilot intervention.</p>
"""),
            ("architecture", "Hardware & Software Architecture", """
<p>The system is architected as a two-tier heterogeneous computing pipeline:</p>
<ul>
  <li><strong>Flight & Actuation Layer (Hard Real-Time):</strong> A Pixhawk flight controller running customized PX4 firmware executes primary motor mixing, attitude EKF3 state estimation, and fail-safe return-to-launch (RTL). An auxiliary <strong>STM32F103</strong> payload controller interfaces via CAN/UART to pulse the high-pressure solenoid valves and monitor pollen tank reservoir pressure.</li>
  <li><strong>High-Level Perception & Mission Layer (Soft Real-Time):</strong> An onboard <strong>Nvidia Jetson Nano</strong> handles camera streaming from a Sony IMX477 sensor, executes a TensorRT-optimized <strong>YOLOv11</strong> target detection network at 30 FPS, and computes closed-loop visual servoing offsets transmitted over MAVSDK via companion computer UART (/dev/ttyTHS1 at 921600 baud).</li>
  <li><strong>Digital Twin Validation (ROS/Gazebo SITL):</strong> Prior to bench and flight testing, every mission profile was verified in a simulated palm plantation environment using Gazebo SITL and ROS nodes, validating obstacle clearance and trajectory re-planning.</li>
</ul>
"""),
            ("design_highlights", "Engineering Highlights & Mechanical Design", """
<p>Key design decisions executed across mechanical, electrical, and firmware domains:</p>
<ul>
  <li><strong>Vibration-Isolated Payload Bay:</strong> Designed custom 3K carbon-fiber plate brackets and SLA-printed TPU dampers in SolidWorks to isolate high-frequency motor vibration (180–220 Hz) from the optical camera and IMU sensors.</li>
  <li><strong>Pneumatic Dispersion Mechanism:</strong> Designed an STM32-actuated micro-solenoid pulse system delivering a 150 ms nitrogen burst, aerosolizing 0.5 g of pollen-talc mixture with uniform cone dispersion.</li>
  <li><strong>Power Distribution Integrity:</strong> Dual isolated power rails (6S 22.2V LiPo for propulsion via 40A BLHeli_32 ESCs; buck-regulated 5V 5A for Jetson Nano and 3.3V for STM32 and optical sensors) preventing inductive back-EMF spikes from corrupting computing logic.</li>
  <li><strong>Fail-Safe Telemetry Watchdog:</strong> Implemented heartbeats at 10 Hz across Jetson, Pixhawk, and ground station. Loss of telemetry triggers instantaneous autonomous loiter and automated RTL after 3.0 seconds.</li>
</ul>
"""),
            ("results", "Bench & Flight Validation Results", """
<p>Extensive field and bench testing confirmed robust operational reliability:</p>
<ul>
  <li>Achieved sub-50 ms end-to-end command latency from vision target acquisition to pneumatic valve triggering.</li>
  <li>Maintained position holding precision within ±8 cm in 15 knot wind conditions using fused RTK-GPS and optical flow.</li>
  <li>YOLOv11 detection achieved 94.2% mAP@0.5 on receptive palm flower clusters under varying tropical sunlight.</li>
</ul>
""")
        ]
    },
    {
        "slug": "l1-adaptive-control-uav",
        "num": "02",
        "badge": "THESIS / HIL SIMULATION",
        "cat_str": "drone software",
        "title": "HIL Testing Adaptive L1 Control for UAV Heavy Payload Drop on STM32F407 (Pixhawk)",
        "subtitle": "Rigorous Control Theoretic Proof and Real-Time Hardware-in-the-Loop Implementation for Sudden Mass Shedding and Aerodynamic Disturbance Rejection",
        "role": "Lead Research Engineer (Undergraduate Thesis)",
        "client": "Institut Teknologi Bandung",
        "period": "2025 – 2026",
        "stack": ["STM32F407", "Pixhawk", "MATLAB / Simulink", "ROS", "Gazebo", "C++", "ArduPilot / PX4", "HIL / SITL"],
        "metrics": [
            ("< 0.8s", "Settling Time Post-Drop"),
            ("40%", "Instant Mass Shedding"),
            ("< 3 deg", "Maximum Attitude Error"),
            ("100 Hz", "Control Loop Rate")
        ],
        "summary": "Developed, proven via Lyapunov stability, and implemented an Adaptive L1 Control architecture with state observers and event-triggered actuation for quadrotors undergoing abrupt heavy payload releases (up to 40% total vehicle mass). Progressed from mathematical derivation and MATLAB simulation to ROS/Gazebo SITL, culminating in hard real-time Hardware-in-the-Loop (HIL) execution on an STM32F407 (Pixhawk) flight computer.",
        "cover_img": "l1-adaptive-drone-testing.jpg",
        "fig1_img": "drone-simulation-console.jpg",
        "fig1_cap": "Figure 1: Hardware-in-the-loop (HIL) telemetry streaming: real-time state observer tracking matched uncertainties during instantaneous mass drop.",
        "fig2_img": "drone-bench-testing.jpg",
        "fig2_cap": "Figure 2: Real-time STM32F407 Pixhawk test bench with hardware pulse capture and disturbance injection.",
        "gallery_imgs": [
            ("l1-adaptive-drone-testing.jpg", "HIL real-time test bench"),
            ("drone-simulation-console.jpg", "Attitude error and Lyapunov convergence"),
            ("drone-bench-testing.jpg", "Flight controller hardware integration")
        ],
        "sections": [
            ("overview", "Control Theory Context & Problem Formulation", """
<p>When an autonomous drone releases a heavy payload (such as an emergency medical package, fire retardant canister, or agricultural sprayer payload), its total mass drops abruptly by 30% to 50% in tens of milliseconds. This step-change instantly invalidates the drone's inertia matrix, center of gravity (CG), and aerodynamic lift-to-thrust equilibrium.</p>
<p>Conventional PID and cascaded linear controllers experience severe control saturation, violent attitude oscillations (up to ±25°), and altitude ballooning that often induces catastrophic motor desynchronization or stall. My thesis investigated designing a robust adaptive controller capable of decoupling adaptation from robustness to guarantee uniform boundedness of system states under abrupt structural variations.</p>
"""),
            ("architecture", "Adaptive L1 Control Architecture & Observer Derivation", """
<p>The control framework is formulated in three core mathematical components:</p>
<ul>
  <li><strong>State Predictor:</strong> Continuously estimates baseline nominal rigid-body drone dynamics using a high-order state space model parameterized by current mass estimate.</li>
  <li><strong>Fast Adaptive Estimation Law:</strong> Employs projection-based adaptive update laws driven by prediction errors, providing rapid adaptation rates without exciting unmodeled high-frequency structural resonances.</li>
  <li><strong>Low-Pass Filter Selection:</strong> A strictly-proper low-pass filter \(D(s)\) band-limits the adaptive control signal to within the actuator bandwidth of the ESC and brushless motors (cutoff frequency tuned at 12 rad/s), preserving phase margin and robust stability margins.</li>
  <li><strong>Event-Triggered Actuation:</strong> Incorporates a Lyapunov-based event-trigger condition that computes new control updates only when Lyapunov function derivative thresholds are approached, reducing microcontroller CPU utilization by 42% on the STM32F407.</li>
</ul>
"""),
            ("design_highlights", "Implementation Pathway: MATLAB to STM32F407 HIL", """
<p>The development lifecycle followed a strict verification ladder:</p>
<ul>
  <li><strong>Mathematical Derivation:</strong> Derived global uniform ultimate boundedness (UUB) via Lyapunov analysis in MATLAB, establishing quantifiable tracking error bounds dependent on filter bandwidth.</li>
  <li><strong>ROS / Gazebo SITL:</strong> Integrated the C++ algorithm into a custom PX4 autopilot flight module and simulated sudden mass jettisoning in Gazebo with realistic sensor noise and turbulence.</li>
  <li><strong>Hardware-in-the-Loop (HIL) on STM32F407:</strong> Flashed the optimized fixed-point / single-precision floating-point C++ control law onto the STM32F407 (Cortex-M4 with FPU @ 168 MHz) on the Pixhawk board. The MCU processed actual sensor feeds and computed motor PWM outputs at 100 Hz in hard real-time while a simulation host fed dynamic kinematics over serial DMA.</li>
</ul>
"""),
            ("results", "Empirical HIL Performance & Rejection Metrics", """
<p>Bench validation against traditional cascaded PID controllers demonstrated dramatic performance gains:</p>
<ul>
  <li><strong>Settling Time:</strong> Restored nominal altitude and attitude equilibrium in <strong>0.78 seconds</strong> post-drop (compared to 3.4 seconds and significant ring-down in cascaded PID).</li>
  <li><strong>Peak Attitude Deviation:</strong> Constrained pitch and roll excursions to within <strong>2.8 degrees</strong> during a 40% instantaneous mass shedding event.</li>
  <li><strong>Stability Guarantee:</strong> Zero motor saturation or desync events observed across 50 consecutive drop trials under simulated 5 m/s crosswind gust injection.</li>
</ul>
""")
        ]
    },
    {
        "slug": "pcb-reflow-conveyor-cv-sorting",
        "num": "03",
        "badge": "EMBEDDED / MECHATRONICS / CV",
        "cat_str": "embedded pcb software",
        "title": "PCB Reflow Heating Conveyor System with CV Defect Sorting",
        "subtitle": "Industrial Automated SMT Reflow Conveyor with STM32 FreeRTOS Closed-Loop PID Thermal Profiling and Raspberry Pi Computer Vision Defect Classification",
        "role": "Firmware & Mechatronics Integration Engineer",
        "client": "Industrial Automation Prototype",
        "period": "2025",
        "stack": ["STM32F103", "FreeRTOS", "Raspberry Pi", "OpenCV", "Python", "PID Control", "I2C / SPI", "SolidWorks"],
        "metrics": [
            ("250 ms", "PID Loop Cycle"),
            ("6 Tasks", "Static FreeRTOS"),
            ("± 2 °C", "Thermal Precision"),
            ("98.4%", "Defect Detection")
        ],
        "summary": "Built a production-grade automated reflow oven prototype combining continuous conveyor mechanics, 4-stage thermal profiling, and real-time computer vision automated optical inspection (AOI). Designed and implemented the STM32F103 firmware on FreeRTOS with 6 statically allocated tasks, hardware watchdog supervisor, 250ms PID temperature regulation, stepper conveyor synchronizer, and high-speed servo sorting mechanism interfaced to a Raspberry Pi camera module.",
        "cover_img": "reflow-oven-bench-setup.png",
        "fig1_img": "reflow-oven-sequencer.gif",
        "fig1_cap": "Figure 1: Automated conveyor sequencer: synchronized stepper transport, dual IR heating zones, cooling chamber, and AOI inspection station.",
        "fig2_img": "reflow-oven-bench-setup.png",
        "fig2_cap": "Figure 2: Complete bench prototype showing STM32 control electronics, solid-state relays (SSRs), thermocouple conditioning, and Raspberry Pi vision rig.",
        "gallery_imgs": [
            ("reflow-oven-bench-setup.png", "Complete bench setup & electronics"),
            ("reflow-oven-sequencer.gif", "Conveyor sequence & servo sorter"),
            ("mini-stm32-pcb-3d.gif", "STM32 controller board")
        ],
        "sections": [
            ("overview", "System Concept & Engineering Responsibilities", """
<p>Small-batch SMT prototype manufacturing requires adherence to strict JEDEC thermal reflow profiles (Preheat, Soak, Reflow peak, and Cool-down) to avoid thermal shock, tombstoning, and solder bridging. Commercial reflow ovens are bulky, open-loop, and lack integrated defect inspection.</p>
<p>I served as the lead firmware and mechatronics engineer for an automated reflow conveyor system. My responsibilities encompassed complete STM32 FreeRTOS firmware architecture, closed-loop PID heating control via Solid State Relays (SSRs), stepper motor conveyor timing, servo-based board rejection mechanism, and serial handshaking with a Raspberry Pi optical inspection station.</p>
"""),
            ("architecture", "FreeRTOS Multi-Tasking Firmware Architecture", """
<p>The STM32F103C8T6 microcontroller runs FreeRTOS with statically allocated memory structures to prevent heap fragmentation in continuous industrial operation:</p>
<ul>
  <li><code>vTaskThermalPID</code> (250 ms period, Priority 4): Reads cold-junction compensated MAX6675 / I2C temperature sensors, computes anti-windup PID error against the active profile phase, and drives zero-crossing SSRs via timed GPIO PWM.</li>
  <li><code>vTaskConveyorControl</code> (50 ms period, Priority 3): Generates acceleration-ramped step pulses for the NEMA 17 stepper driver, ensuring smooth transport without dislodging unfused SMD components.</li>
  <li><code>vTaskServoSort</code> (Event-driven queue, Priority 3): Actuates the dual-position pneumatic/servo divert gate to route inspected PCBs into 'PASS' or 'REWORK' bins based on AOI vision flags.</li>
  <li><code>vTaskVisionBridge</code> (10 ms period, Priority 2): Parses structured JSON/binary packets from the Raspberry Pi over USART1 DMA, exchanging board IDs, inspection results, and line velocity.</li>
  <li><code>vTaskUIState</code> (100 ms period, Priority 1): Updates status OLED display, emergency e-stop states, and diagnostic LEDs.</li>
  <li><code>vTaskWatchdog</code> (500 ms period, Priority 5): Periodically kicks the independent hardware watchdog (IWDG). Failure in any of the 5 worker tasks halts heating instantly and raises audible alarms.</li>
</ul>
"""),
            ("design_highlights", "Computer Vision AOI & Mechatronics Integration", """
<p>Key electromechanical and optical engineering highlights:</p>
<ul>
  <li><strong>Defect Detection Pipeline:</strong> The Raspberry Pi camera captures top-down macro images under polarized ring lighting as the board exits the cooling zone. An OpenCV + PyTorch classification pipeline evaluates pad alignment, solder bridges, and component skew/tombstone defects.</li>
  <li><strong>Thermal Enclosure Design:</strong> Modeled the chassis in SolidWorks, incorporating ceramic fiber insulation, quartz infrared heating elements, and a high-temperature stainless steel mesh belt conveyor.</li>
  <li><strong>Zero-Cross Triac/SSR Firing:</strong> Integrated zero-cross SSR control to eliminate EMI switching noise on the 220V AC mains line that could induce jitter on the thermocouple analog lines.</li>
</ul>
"""),
            ("results", "Thermal Precision & Quality Sorting Results", """
<p>Empirical testing across lead-free SAC305 solder paste profiles demonstrated excellent repeatability:</p>
<ul>
  <li>Maintained preheat ramp rate strictly at 1.5–2.0 °C/sec and reflow peak at 245 °C ± 2 °C across the entire heating chamber length.</li>
  <li>Achieved 98.4% true-positive classification accuracy on solder bridges and component misalignment during conveyor speeds up to 15 mm/sec.</li>
  <li>Zero firmware crashes or task starvation over 48 hours of continuous endurance thermal cycling.</li>
</ul>
""")
        ]
    },
    {
        "slug": "mipi-bridge-board",
        "num": "04",
        "badge": "4-LAYER HIGH-SPEED PCB",
        "cat_str": "pcb hardware",
        "title": "MIPI DSI to HDMI/LVDS Bridge Board for ESP32-P4",
        "subtitle": "High-Speed 4-Layer PCB with Controlled Differential Impedance, LT8912B Bridge IC, Multi-Voltage Power Tree, and Comprehensive ESD Protection",
        "role": "Lead Hardware & PCB Design Engineer",
        "client": "High-Performance Embedded Graphics",
        "period": "2025 – 2026",
        "stack": ["KiCad", "LT8912B", "ESP32-P4", "4-Layer PCB", "Impedance Control", "ESD Protection", "High-Speed Layout"],
        "metrics": [
            ("90 Ω", "Diff Impedance"),
            ("1080p60", "Video Output"),
            ("4-Layer", "JLC04161H Stackup"),
            ("45 × 65 mm", "Compact Form Factor")
        ],
        "summary": "Designed a custom 4-layer high-speed interface PCB (45 × 65 mm) converting MIPI DSI display lanes from the ESP32-P4 processor to standard HDMI and LVDS display outputs via the LT8912B bridge IC. Engineered the JLC04161H-7628 controlled-impedance stackup, multi-rail power distribution (1.8V, 3.3V, 5V), 9-channel LBSS138 bi-directional level shifters, and low-capacitance RClamp0524P ESD protection.",
        "cover_img": "mipi-bridge-3d.png",
        "fig1_img": "mipi-bridge-schematic.jpg",
        "fig1_cap": "Figure 1: Complete circuit schematic: LT8912B MIPI-to-HDMI bridge, level-shifting network, power LDOs, and ESD clamping.",
        "fig2_img": "mipi-bridge-3d.png",
        "fig2_cap": "Figure 2: 3D CAD render of the 4-layer PCB highlighting high-speed length-matched differential pairs and HDMI receptacle.",
        "gallery_imgs": [
            ("mipi-bridge-3d.png", "3D PCB rendering"),
            ("mipi-bridge-schematic.jpg", "Complete schematic sheet"),
            ("atmega128-dev-board-3d.png", "PCB fabrication comparison")
        ],
        "sections": [
            ("overview", "Design Objective & High-Speed Challenges", """
<p>The Espressif ESP32-P4 RISC-V SoC introduces hardware MIPI DSI interfaces capable of driving high-resolution displays. However, developing industrial and consumer displays often requires interfacing to standard HDMI monitors or LVDS industrial panels.</p>
<p>I engineered a dedicated 45 × 65 mm carrier board centered on the LonTium LT8912B bridge IC. The board bridges 2-lane / 4-lane MIPI DSI inputs (up to 1.5 Gbps per lane) to HDMI 1.4b (up to 1080p @ 60Hz) or single-link LVDS, solving high-speed signal integrity, multi-voltage domain sequencing, and thermal dissipation in an ultra-compact footprint.</p>
"""),
            ("architecture", "4-Layer Stackup & Controlled Impedance Routing", """
<p>The board utilizes the JLCPCB <strong>JLC04161H-7628</strong> 4-layer stackup: Layer 1 (Top Signal) — Layer 2 (Solid GND) — Layer 3 (Power Plane) — Layer 4 (Bottom Signal):</p>
<ul>
  <li><strong>MIPI DSI Differential Pairs:</strong> Routed on Layer 1 over an unbroken Layer 2 GND reference plane with 90 Ω differential impedance (trace width 0.15 mm, gap 0.18 mm). Intra-pair skew was matched to within 0.1 mm to eliminate phase distortion at gigabit data rates.</li>
  <li><strong>HDMI TMDS Lines:</strong> Length-matched 100 Ω differential pairs routed with gentle 45-degree chamfers, avoiding via transitions between layers to prevent impedance discontinuities and return path disruptions.</li>
  <li><strong>Continuous Ground Planes:</strong> Layer 2 is dedicated purely to analog and digital ground return paths, guaranteeing minimum loop area for RF return currents.</li>
</ul>
"""),
            ("design_highlights", "Power Tree, Level Shifters & ESD Protection", """
<p>Crucial circuit architecture highlights executed on the schematic:</p>
<ul>
  <li><strong>Triple-Rail Power Supply Tree:</strong> Designed an input filtering and distribution network accepting 5V from USB/Host, stepping down to 3.3V (IO logic) and ultra-low-noise 1.8V (LT8912B analog PLL and core) using dedicated low-dropout regulators (LDOs) with ferrite bead pi-filters (\(\pi\)-filter) to attenuate high-frequency switching hash.</li>
  <li><strong>Bi-Directional Level Shifting:</strong> Implemented a 9-channel level shifter array using LBSS138 N-channel MOSFETs with 10kΩ pull-up resistors to seamlessly interface 1.8V LT8912B sideband controls with 3.3V ESP32-P4 GPIO lines (I2C configuration bus, HPD, CEC).</li>
  <li><strong>ESD Clamping:</strong> Placed low-capacitance (0.3 pF) <strong>RClamp0524P</strong> TVS diode arrays directly adjacent to the HDMI Type-A connector pins, protecting sensitive differential silicon from ±15kV human-body electrostatic discharge without degrading gigabit eye diagrams.</li>
</ul>
"""),
            ("results", "Signal Integrity Verification & Output Quality", """
<p>Validation across lab instrumentation confirmed first-pass fabrication success:</p>
<ul>
  <li>Verified clean 1080p @ 60Hz video streaming from ESP32-P4 MIPI DSI framebuffer onto standard HDMI monitors with zero artifacting or line jitter.</li>
  <li>Measured power rail ripple below 12 mV peak-to-peak on the critical 1.8V PLL supply under full 1.5 Gbps lane transmission.</li>
  <li>Full pass on DRC/DFM checks with zero unrouted nets, 0.127 mm minimum clearance, and full copper balance across both outer layers.</li>
</ul>
""")
        ]
    },
    {
        "slug": "fpga-cnn-eye-state",
        "num": "05",
        "badge": "FPGA / VERILOG / INT8",
        "cat_str": "fpga hardware software",
        "title": "Basys 3 FPGA CNN Eye-State Classifier (Artix-7)",
        "subtitle": "Bit-Exact Hardware Accelerators for INT8 Quantized Convolutional Neural Network on Xilinx Artix-7 with Zero DSP Slice Consumption",
        "role": "FPGA Digital Design Engineer",
        "client": "Digital Systems Lab / Academic Research",
        "period": "2025",
        "stack": ["Verilog HDL", "Xilinx Artix-7", "Basys 3", "Vivado", "PyTorch", "INT8 Quantization", "Fixed-Point DSP"],
        "metrics": [
            ("98.1%", "Classification Accuracy"),
            ("100%", "Bit-Exact vs Python"),
            ("0 DSP", "Pure LUT/FF Architecture"),
            ("100 MHz", "Pipeline Clock Rate")
        ],
        "summary": "Designed, synthesized, and verified an integer-only Convolutional Neural Network (CNN) accelerator in Verilog HDL on a Digilent Basys 3 (Xilinx Artix-7 XC7A35T) FPGA for driver drowsiness eye-state classification (open vs closed). Achieved 98.1% test accuracy and a bit-exact 100% numerical match with a PyTorch INT8 quantized golden model using an ultra-efficient single-MAC pipelined datapath that consumed zero dedicated DSP slices.",
        "cover_img": "fpga-cnn-block-diagram.png",
        "fig1_img": "fpga-cnn-architecture.png",
        "fig1_cap": "Figure 1: Hardware datapath block diagram: input BRAM buffer, single-MAC multiply-accumulate unit, ReLU thresholding, and state sequencer.",
        "fig2_img": "fpga-cnn-block-diagram.png",
        "fig2_cap": "Figure 2: Top-level Verilog hierarchy: control FSM, weight ROMs, feature map scratchpad, and classification decision logic.",
        "gallery_imgs": [
            ("fpga-cnn-block-diagram.png", "Top-level block diagram"),
            ("fpga-cnn-architecture.png", "Pipelined datapath architecture"),
            ("mini-stm32-pcb-3d.gif", "Embedded integration reference")
        ],
        "sections": [
            ("overview", "Edge AI Acceleration & Resource Challenge", """
<p>Deploying deep learning on edge devices for real-time safety systems (such as driver drowsiness monitoring) demands ultra-low power consumption and microsecond-level latency. While GPUs and high-end SoCs carry substantial thermal and monetary costs, low-cost FPGAs like the Xilinx Artix-7 (Basys 3) provide an ideal target if networks are properly optimized.</p>
<p>The goal was to design a self-contained, fully hardware-accelerated CNN classifier capable of ingesting eye-region image matrices and outputting binary 'Open' or 'Closed' eye states with high reliability, minimal footprint, and zero reliance on external memory chips or DSP slices.</p>
"""),
            ("architecture", "INT8 Quantization & Pipelined Single-MAC Datapath", """
<p>The architecture transitions deep learning from floating-point theory to pure digital logic:</p>
<ul>
  <li><strong>Quantization Strategy:</strong> Trained a custom lightweight CNN in PyTorch on 24 × 24 grayscale eye crops. Quantized all weights and activation tensors from 32-bit floating point to signed 8-bit integers (INT8) using symmetric uniform quantization with power-of-two scaling factors, eliminating expensive division in hardware.</li>
  <li><strong>Single-MAC Time-Multiplexed Engine:</strong> Rather than unrolling massive parallel multiplier arrays that exhaust FPGA resources, I designed an optimized single-MAC (Multiply-Accumulate) datapath operating at 100 MHz. The unit features an 8×8 signed multiplier feeding a 24-bit accumulator with saturation logic.</li>
  <li><strong>Weight ROM & Input BRAM:</strong> Stored static quantized weights in distributed ROM blocks, while intermediate feature activations reside in dual-port Block RAM (BRAM) configured as ping-pong buffers.</li>
</ul>
"""),
            ("design_highlights", "Verilog Implementation & Golden Model Verification", """
<p>Key digital design techniques executed in Vivado:</p>
<ul>
  <li><strong>Zero DSP Slice Usage:</strong> The entire datapath was synthesized using pure LUT and Flip-Flop logic without utilizing a single DSP48E1 slice. This leaves the FPGA's DSP slices completely free for auxiliary DSP, video scaling, or motor control tasks.</li>
  <li><strong>Bit-Exact Verification:</strong> Constructed an automated Python testbench wrapper generating binary test vectors from PyTorch. In ModelSim/Vivado simulation, the Verilog output matched the Python integer golden model across 1,000 test cases with 100% bit-exact equivalence.</li>
  <li><strong>Control FSM:</strong> A 5-state Mealy/Moore finite state machine orchestrates pixel streaming, convolution window sliding, max pooling address generation, dense layer dot products, and argmax classification.</li>
</ul>
"""),
            ("results", "Synthesis Metrics & Classification Accuracy", """
<p>Implementation on the Basys 3 board delivered compelling metrics:</p>
<ul>
  <li>Achieved <strong>98.1% classification accuracy</strong> on the test dataset, identical to the floating-point reference model within 0.2%.</li>
  <li>Executed inference in under <strong>1.4 ms per frame</strong> at 100 MHz, easily exceeding 700 frames-per-second throughput capability.</li>
  <li>Consumed less than 28% of available LUTs and 18% of BRAM slices on the Artix-7 XC7A35T, with total on-chip power consumption under 140 mW.</li>
</ul>
""")
        ]
    },
    {
        "slug": "atmega128-dev-board",
        "num": "06",
        "badge": "MCU HARDWARE / DEVELOPMENT BOARD",
        "cat_str": "pcb embedded hardware",
        "title": "ATmega128 Development Board",
        "subtitle": "Compact 60 × 35 mm 2-Layer System Board with USB-C 5.1k Pulldowns, Isolated AVCC LC Filter, CH340C Auto-Reset, and Length-Matched 90Ω Differential Pairs",
        "role": "Hardware & PCB Design Engineer",
        "client": "Personal Engineering Project",
        "period": "2025 – 2026",
        "stack": ["KiCad", "ATmega128A", "CH340C", "USB Type-C", "LC Filter", "PCB Layout", "Hardware Prototyping"],
        "metrics": [
            ("60 × 35 mm", "Compact Size"),
            ("5.1 kΩ", "Type-C CC Sink"),
            ("10 µH", "AVCC LC Filter"),
            ("90 Ω", "USB Diff Pairs")
        ],
        "summary": "Designed a high-reliability, pocket-sized (60 × 35 mm) development board centered on the classic 8-bit AVR ATmega128A microcontroller. Overcame legacy DIP pin limitations by engineering a robust 2-layer layout featuring modern USB Type-C power and data, 5.1kΩ pulldown configuration, dedicated 10µH + 100nF LC analog power filtering for the 10-bit ADC, CH340C DTR auto-reset bootloader circuitry, and 90Ω USB differential traces.",
        "cover_img": "atmega128-dev-board-3d.png",
        "fig1_img": "atmega128-dev-board-schematic.jpg",
        "fig1_cap": "Figure 1: Full schematic: ATmega128 core, USB-C interface, CH340C bridge with DTR auto-reset, crystal tank, and LC analog rail.",
        "fig2_img": "atmega128-dev-board-3d.png",
        "fig2_cap": "Figure 2: 3D CAD visualization showing compact dual header pinout, crystal oscillator, decoupling layout, and Type-C receptacle.",
        "gallery_imgs": [
            ("atmega128-dev-board-3d.png", "3D CAD model"),
            ("atmega128-dev-board-schematic.jpg", "Complete circuit schematic"),
            ("mini-stm32-pcb-3d.gif", "Compact board comparison")
        ],
        "sections": [
            ("overview", "Motivation & Hardware Objectives", """
<p>The ATmega128A offers 128KB of Flash, 53 GPIO lines, dual hardware USARTs, and abundant timers, making it a workhorse for embedded systems education and rugged industrial controllers. However, commercial breakout boards are often bulky, rely on obsolete mini-USB/barrel connectors, and suffer from noisy ADC readings due to inadequate analog filtering.</p>
<p>I engineered a modern, ultra-compact (60 × 35 mm) breakout board that standardizes on USB Type-C, incorporates proper analog domain isolation, and enables seamless one-click programming via an onboard CH340C bridge.</p>
"""),
            ("architecture", "Analog Power Integrity & USB-C Implementation", """
<p>Design execution focused on signal integrity and power robustness:</p>
<ul>
  <li><strong>USB Type-C CC Configuration:</strong> Implemented discrete 5.1 kΩ (±1%) pulldown resistors on pins CC1 and CC2. This configures the board as a standard UFP (Upstream Facing Port) sink device, allowing safe power negotiation from modern USB-C PD and E-marked cables without violating the Type-C specification.</li>
  <li><strong>AVCC LC Filter Isolation:</strong> The internal 10-bit successive approximation ADC on the ATmega128 is highly susceptible to digital switching noise. I designed an analog LC low-pass filter consisting of a 10 µH SMD inductor and a 100 nF ceramic capacitor between VCC and AVCC, effectively attenuating digital rail hash above 150 kHz.</li>
  <li><strong>Controlled 90 Ω USB Pairs:</strong> Routed the USB D+ and D- signals as tightly coupled 90 Ω differential pairs with 22 Ω series termination resistors adjacent to the CH340C IC to prevent signal reflection.</li>
</ul>
"""),
            ("design_highlights", "Auto-Reset Circuitry & Clock Oscillator Layout", """
<p>Detailed circuit and layout considerations:</p>
<ul>
  <li><strong>DTR Capacitive Auto-Reset:</strong> Integrated a 100 nF ceramic capacitor in series with the CH340C DTR line and a 10 kΩ pull-up with 1N4148 clamping diode on the ATmega128 RESET pin. This generates a crisp active-low pulse during UART connection, enabling seamless bootloader upload from Arduino IDE / AVRDUDE without manual reset button pressing.</li>
  <li><strong>16 MHz Crystal Oscillator Tank:</strong> Placed the 16 MHz HC-49SM crystal and 22 pF load capacitors immediately adjacent to pins XTAL1 and XTAL2, enclosed by a continuous ground guard ring and isolated from high-speed digital switching tracks.</li>
  <li><strong>Breakout Accessibility:</strong> All 53 GPIO pins, ISP programming header (MOSI, MISO, SCK, RESET), and power rails are routed to standard 2.54 mm dual breadboard-friendly pin headers.</li>
</ul>
"""),
            ("results", "Hardware Testing & ADC Verification", """
<p>Assembled and bench-tested prototype boards confirmed clean operation:</p>
<ul>
  <li>Demonstrated 100% reliable sketch flashing at 115200 baud via USB Type-C across Windows, macOS, and Linux platforms.</li>
  <li>Measured ADC ENOB (Effective Number of Bits) improvement from 8.2 bits (unfiltered) to <strong>9.7 bits</strong> with the LC filter network, virtually eliminating digital switching noise from sensor readings.</li>
  <li>Thermal imaging verified even heat dissipation across the 500mA AMS1117-3.3/5.0 LDO regulator under maximum digital output loading.</li>
</ul>
""")
        ]
    },
    {
        "slug": "industrial-pid-delivery-box",
        "num": "07",
        "badge": "EMBEDDED / IOT / POWER",
        "cat_str": "embedded iiot software",
        "title": "Control Temperature Food Delivery Box",
        "subtitle": "Dual-Core ESP32 Real-Time Thermoelectric Climate Control with FreeRTOS, Custom PDB Schematic, BMS Protection, and Remote Mobile App",
        "role": "Lead IoT, Embedded Systems & Hardware Engineer",
        "client": "Smart Food Logistics Prototype",
        "period": "2025",
        "stack": ["ESP32", "FreeRTOS", "C++ / Arduino", "PID Control", "Peltier (TEC)", "PTC Heater", "KiCad", "Kodular"],
        "metrics": [
            ("23 °C / 45 °C", "Dual Setpoints"),
            ("± 0.5 °C", "Steady-State Error"),
            ("3S BMS", "Power Distribution"),
            ("Dual-Core", "FreeRTOS Pipeline")
        ],
        "summary": "Built an intelligent temperature-controlled food delivery box engineered around a dual-core ESP32 running FreeRTOS. Core 0 executes closed-loop PID thermal control holding stable setpoints of 23°C (cold storage via TEC Peltier) and 45°C (hot delivery via PTC air heating), while Core 1 handles wireless telemetry and mobile app communication. Designed a custom Power Distribution Board (PDB) featuring INA219 battery monitoring, BMS protection, and MOSFET load switches.",
        "cover_img": "delivery-box-closed.gif",
        "fig1_img": "delivery-box-exploded.gif",
        "fig1_cap": "Figure 1: Exploded assembly of the 40 × 30 × 27 cm insulated enclosure showing airflow ducting, Peltier heat sinks, and electronics bay.",
        "fig2_img": "delivery-box-pdb-schematic.gif",
        "fig2_cap": "Figure 2: Power Distribution Board (PDB) schematic: 3S Li-ion battery management, INA219 current monitoring, MP1584 buck regulators, and MOSFET drivers.",
        "gallery_imgs": [
            ("delivery-box-closed.gif", "Insulated enclosure assembly"),
            ("delivery-box-exploded.gif", "Exploded mechanical view"),
            ("delivery-box-app.jpg", "Mobile app live monitoring UI")
        ],
        "sections": [
            ("overview", "Project Context & Thermal Challenge", """
<p>Maintaining hot meals above the food-safety danger zone (>60°C or regulated 45°C holding) and cold groceries below 23°C during long motorcycle delivery routes in tropical climates requires active climate regulation. Passive insulated bags degrade within 30 minutes, resulting in food spoilage or compromised quality.</p>
<p>I engineered an active climate-regulated container featuring independent heating and cooling loops, robust Li-ion battery management with supplementary solar input, and real-time smartphone telemetry.</p>
"""),
            ("architecture", "Dual-Core FreeRTOS Firmware & Control Pipeline", """
<p>The ESP32 firmware leverages symmetric multiprocessing (SMP) across both Xtensa LX6 cores:</p>
<ul>
  <li><strong>Core 0 (Thermal Control Task):</strong> Dedicated exclusively to reading calibrated DHT22 / DS18B20 digital sensors at 1 Hz, executing a PID anti-windup algorithm, and outputting PWM to gate high-current MOSFET switches controlling the 12V 60W PTC heater and TEC1-12706 Peltier cooler.</li>
  <li><strong>Core 1 (IoT & Network Task):</strong> Manages Bluetooth LE and Wi-Fi connections, serving an asynchronous WebSockets interface to a custom Android mobile application built with Kodular. Transmits live chamber temperature, humidity, battery percentage, and solar charge status.</li>
  <li><strong>Hardware Watchdog Timer:</strong> Configured a hardware watchdog that automatically resets the microcontroller if either core deadlocks, safely de-energizing heating elements to prevent thermal runaway.</li>
</ul>
"""),
            ("design_highlights", "Custom Power Distribution Board (PDB) Schematic", """
<p>To power both digital logic and high-draw thermal elements safely, I designed a dedicated PDB:</p>
<ul>
  <li><strong>Battery Management & Monitoring:</strong> Powered by a 3S 12.6V Li-ion battery pack with an integrated hardware BMS circuit for over-current, short-circuit, and undervoltage cutoff. Integrated an <strong>INA219</strong> high-side I2C current/voltage sensor to track power consumption and state-of-charge.</li>
  <li><strong>Regulated Power Rails:</strong> Stepped down 12V raw battery power to 5V (using a high-efficiency MP1584 buck converter) for logic and cooling fans, and 3.3V for the ESP32.</li>
  <li><strong>Logic-Level MOSFET Load Switching:</strong> Implemented low-resistance IRLZ44N N-channel MOSFETs with optocoupler gate drivers and flyback protection diodes to switch inductive blower fans and resistive heating elements without injecting transients into the digital ground.</li>
</ul>
"""),
            ("results", "Thermal Regulation & Battery Life Performance", """
<p>Empirical testing inside the 40 × 30 × 27 cm insulated enclosure verified strong thermal performance:</p>
<ul>
  <li>Maintained steady-state temperature within <strong>±0.5 °C</strong> of target setpoints (23 °C cooling and 45 °C warming) under 34 °C ambient tropical sunlight.</li>
  <li>Achieved over <strong>3.5 hours of continuous active regulation</strong> on a single battery charge, extended by 45 minutes with the top-mounted solar auxiliary panel.</li>
  <li>Seamless mobile telemetry updating every 1.0 second with remote target setpoint adjustments.</li>
</ul>
""")
        ]
    },
    {
        "slug": "automotive-sensor-wire-harness",
        "num": "08",
        "badge": "AUTOMOTIVE R&D / MANUFACTURING",
        "cat_str": "hardware",
        "title": "Sensor Wire Harness: Drawing, BOM & Crimp Specification",
        "subtitle": "Automotive Sensor Wire Harness Assembly for Vehicle Engine Bay Applications with Complete Engineering Drawings, BOM Verification, and Crimp Pull-Test Specs",
        "role": "R&D Electronics Engineering Intern",
        "client": "PT Hana Master Jaya (Automotive Tier-1 Manufacturer)",
        "period": "March – May 2026",
        "stack": ["Wire Harness", "AutoCAD", "BOM Verification", "Crimp Height Spec", "JIS C 2805", "Automotive Standards"],
        "metrics": [
            ("15 Circuits", "Crimped & Sealed"),
            ("3-Leg T", "Harness Topology"),
            ("JIS C 2805", "Tensile Standard"),
            ("5 Clamps", "Chassis Retention")
        ],
        "summary": "Contributed to the engineering development and manufacturing documentation of a Rev. 0 prototype automotive sensor wire harness during an R&D internship at PT Hana Master Jaya. The harness features a 3-leg T-junction linking 8-pin, 3-pin, and dual 2-pin sealed automotive connectors with 15 circuits. Prepared isometric and manufacturing drawings, verified the Bill of Materials (BOM), and established crimp height/width tolerances per automotive standards.",
        "cover_img": "wire-harness-top.jpg",
        "fig1_img": "wire-harness-iso.gif",
        "fig1_cap": "Figure 1: Isometric engineering drawing (1:5 scale) showing 3-leg T-geometry, branch lengths, and connector callouts.",
        "fig2_img": "wire-harness-top.jpg",
        "fig2_cap": "Figure 2: Top-view manufacturing layout detailing corrugated conduit, vinyl sleeving, heat-shrink transitions, and mounting clamps.",
        "gallery_imgs": [
            ("wire-harness-top.jpg", "Top manufacturing layout"),
            ("wire-harness-iso.gif", "Isometric 1:5 drawing"),
            ("sap-flow-board.gif", "Sensor wiring integration")
        ],
        "sections": [
            ("overview", "Industrial Context & Engineering Scope", """
<p>Automotive wire harnesses are safety-critical assemblies that operate in hostile engine-bay environments characterized by high vibration, extreme temperature cycling (-40°C to +125°C), moisture ingress, and chemical exposure (fuel, oil, coolant). A single poor crimp or unsealed connector terminal can lead to sensor failure or vehicle stoppage.</p>
<p>During my internship in the R&D department at <strong>PT Hana Master Jaya</strong>, I supported the engineering team in developing the complete drawing package, Bill of Materials (BOM), and crimping quality specifications for a new automotive sensor wire harness (Rev. 0).</p>
"""),
            ("architecture", "Harness Topology & Mechanical Protection", """
<p>The harness links multiple engine-bay sensors into the main ECU vehicle backbone:</p>
<ul>
  <li><strong>T-Shaped 3-Leg Architecture:</strong> Features a primary trunk terminating in an 8-pin sealed female connector, splitting into three branch legs with an intermediate 3-pin connector and two 2-pin waterproof sensor plugs.</li>
  <li><strong>Circuit Count:</strong> Integrates 15 discrete automotive-grade thin-wall cross-linked polyethylene (AVSS/FLRY) insulated conductors with designated color-coding for sensor power, ground, and analog/PWM signals.</li>
  <li><strong>Harsh Environment Protection:</strong> High-impact polypropylene corrugated split conduit protects main wire runs, while flexible vinyl tubing and adhesive-lined heat shrink enclose junctions. Five chassis mounting clips ensure vibration damping and prevent chafing against sheet metal.</li>
</ul>
"""),
            ("design_highlights", "BOM Verification & Crimping Specifications", """
<p>Key technical contributions executed during the design validation phase:</p>
<ul>
  <li><strong>Drawing Package Preparation:</strong> Supported the senior drafter in producing detailed isometric (1:5), top, and cross-sectional views with precise dimensional tolerances, connector pinouts, and callout tables.</li>
  <li><strong>BOM Cross-Verification:</strong> Cross-checked the comprehensive Bill of Materials against physical assembly prototypes—verifying terminal part numbers, wire gauge sizes (0.5 mm² and 0.85 mm²), silicone wire seals, rubber boots, and conduit diameters.</li>
  <li><strong>Crimp Height & Width Calculation:</strong> Defined critical crimp height (C/H) and crimp width (C/W) specifications for conductor and insulation barrels, referencing manufacturer terminal application tooling guidelines to guarantee gas-tight micro-welds without severed wire strands.</li>
  <li><strong>Tensile Retention Testing:</strong> Established quality pull-test criteria adhering to <strong>JIS C 2805</strong> standards, validating that crimped terminal joints withstand required tensile retention forces prior to wire rupture.</li>
</ul>
"""),
            ("results", "Production Release & Manufacturing Readiness", """
<p>The documentation package was successfully approved for pre-production trial tooling:</p>
<ul>
  <li>Delivered zero-error BOM and wiring schematics adopted into the factory ERP and assembly jig tooling.</li>
  <li>Standardized crimp validation protocols adopted on the crimping press test benches, ensuring repeatable contact resistance below 5 mΩ.</li>
  <li>Verified mechanical fitment and clearance on engine mockup jigs with optimal routing slack and strain relief.</li>
</ul>
""")
        ]
    },
    {
        "slug": "fan-speed-controller",
        "num": "09",
        "badge": "RISC-V / ANALOG / PWM",
        "cat_str": "pcb embedded hardware",
        "title": "CH32V003 RISC-V Fan Speed Controller",
        "subtitle": "Low-Cost Intelligent 4-Pin Fan Controller on CH32V003 RISC-V Microcontroller with PC817 Optoisolation, 25kHz PWM, and Reverse Polarity Protection",
        "role": "Embedded Hardware & Firmware Engineer",
        "client": "Thermal Management Hardware",
        "period": "2025",
        "stack": ["CH32V003", "RISC-V", "KiCad", "PC817", "PWM Control", "Closed-Loop PID", "Analog Circuit Design"],
        "metrics": [
            ("25 kHz", "Standard Fan PWM"),
            ("1000 V", "Galvanic Isolation"),
            ("10-cent", "RISC-V Core"),
            ("± 20 RPM", "Closed-Loop Accuracy")
        ],
        "summary": "Engineered a low-cost, intelligent 4-pin cooling fan speed controller around the ultra-affordable WCH CH32V003 RISC-V microcontroller. Implements 25kHz ultrasonic PWM duty cycle generation, closed-loop tachometer RPM feedback, PC817 optocoupler galvanic isolation between the noisy 12V motor supply and 3.3V MCU digital logic, and 1N4007 reverse polarity diode protection.",
        "cover_img": "fan-controller-board-top.jpg",
        "fig1_img": "fan-controller-schematic.gif",
        "fig1_cap": "Figure 1: Full schematic: CH32V003 MCU, PC817 optoisolation, 25kHz PWM driver stage, tachometer pull-up, and input protection.",
        "fig2_img": "fan-controller-board-bot.jpg",
        "fig2_cap": "Figure 2: Fabricated double-sided PCB bottom copper layer showing isolated ground returns and compact surface-mount routing.",
        "gallery_imgs": [
            ("fan-controller-board-top.jpg", "Top assembled PCB"),
            ("fan-controller-board-bot.jpg", "Bottom PCB traces"),
            ("fan-controller-schematic.gif", "Circuit schematic diagram")
        ],
        "sections": [
            ("overview", "Design Concept & Industrial Motivation", """
<p>Modern industrial electronics enclosures and server racks require quiet, energy-efficient cooling that dynamically adjusts fan RPM based on ambient temperature sensors rather than running fans at a static, noisy 100% duty cycle. Furthermore, 12V DC cooling fans generate substantial inductive kickback and brush commutating electrical noise that can easily reset sensitive microcontrollers.</p>
<p>I designed a compact, robust fan controller board built around the ultra-cost-effective ($0.10) <strong>CH32V003</strong> RISC-V microcontroller, featuring optical isolation, reverse polarity protection, and closed-loop speed stabilization.</p>
"""),
            ("architecture", "Isolated Circuit Architecture & Power Protection", """
<p>The electrical design isolates power and logic domains to maximize noise immunity:</p>
<ul>
  <li><strong>Optocoupled Signal Interface:</strong> Integrated a <strong>PC817</strong> optocoupler to drive the fan's 25kHz PWM input pin. This provides 1000V+ of galvanic isolation, keeping ground loops and high-current fan motor noise completely separated from the sensitive 3.3V microcontroller supply.</li>
  <li><strong>Input Reverse Polarity & Clamping:</strong> Placed a high-current <strong>1N4007</strong> power diode in series with the 12V input jack, protecting against accidental reverse power polarity. A bidirectional clamping capacitor and TVS diode absorb automotive-style load dump transients.</li>
  <li><strong>Onboard Voltage Regulation:</strong> Utilized a high-voltage input LDO to step down the 12V DC input to a clean 3.3V logic supply for the CH32V003 MCU.</li>
</ul>
"""),
            ("design_highlights", "RISC-V Firmware & 25kHz Timer Capture", """
<p>Firmware implementation details on the QingKe 32-bit RISC-V core:</p>
<ul>
  <li><strong>25 kHz Ultrasonic PWM Generation:</strong> Configured advanced-control Timer 1 to produce standard Intel 4-pin fan compliant 25 kHz PWM. At 25 kHz, switching frequencies are well outside the human auditory spectrum, eliminating annoying coil whine.</li>
  <li><strong>Tachometer Frequency Capture:</strong> The fan's open-collector tachometer pulse output is pulled up to 3.3V and routed into a timer capture channel with hardware glitch filtering. Each revolution outputs 2 pulses; the firmware computes instantaneous RPM with ±20 RPM resolution.</li>
  <li><strong>Closed-Loop PID Regulation:</strong> Executes a lightweight fixed-point PID loop that adjusts PWM duty cycle to maintain precise target RPM regardless of supply voltage fluctuations or air filter backpressure.</li>
</ul>
"""),
            ("results", "Bench Testing & Acoustic Results", """
<p>Prototype evaluation with high-performance 12V server fans confirmed exceptional stability:</p>
<ul>
  <li>Smooth speed modulation from 10% minimum idle speed (350 RPM) to 100% full blast (4,800 RPM) with linear tachometer tracking.</li>
  <li>Total absence of inductive back-EMF or voltage dips on the 3.3V MCU digital rail during aggressive fan acceleration and stall events.</li>
  <li>Board survived repeated reverse polarity connection tests at 15V without component damage.</li>
</ul>
""")
        ]
    },
    {
        "slug": "usbc-boost-module",
        "num": "10",
        "badge": "POWER ELECTRONICS / DC-DC",
        "cat_str": "pcb hardware",
        "title": "USB-C to 12V Boost Module (CX8823)",
        "subtitle": "High-Efficiency Step-Up DC-DC Converter Delivering 12V 1.5A from 5V USB-C with 3.3µH Shielded Inductor, TVS Protection, and Low Ripple",
        "role": "Power Electronics & PCB Designer",
        "client": "Hardware Tooling / Modular Power",
        "period": "2025",
        "stack": ["KiCad", "CX8823", "DC-DC Boost", "TVS Surge Protection", "SMD Inductor", "Power Integrity", "PCB Layout"],
        "metrics": [
            ("12 V / 1.5 A", "Output Rating"),
            ("92%", "Peak Efficiency"),
            ("< 25 mV", "Output Ripple"),
            ("3.3 µH", "Shielded Inductor")
        ],
        "summary": "Designed a high-density step-up DC-DC converter module stepping up 5V from any standard USB-C port to a regulated 12V 1.5A output for powering routers, lab instruments, and 12V LED drivers. Centered on the CX8823 synchronous boost regulator, the board features a 3.3µH high-current power inductor, 470µF low-ESR solid electrolytic capacitor, input TVS diode surge clamping, and DNP jumper options.",
        "cover_img": "usbc-boost-3d.gif",
        "fig1_img": "usbc-boost-schematic.gif",
        "fig1_cap": "Figure 1: Boost converter schematic: CX8823 switching loop, feedback resistor divider, TVS protection (Z1/D1), and bulk filter.",
        "fig2_img": "usbc-boost-module-top.jpg",
        "fig2_cap": "Figure 2: Top view of assembled module showing compact surface-mount component placement and thermal copper pour.",
        "gallery_imgs": [
            ("usbc-boost-3d.gif", "3D CAD model"),
            ("usbc-boost-module-top.jpg", "Top PCB assembly"),
            ("usbc-boost-module-bot.jpg", "Bottom PCB copper plane")
        ],
        "sections": [
            ("overview", "Design Challenge & Use Case", """
<p>Field technicians, embedded engineers, and IoT deployers frequently need clean 12V DC power in situations where only 5V USB power banks or laptop ports are available. Inexpensive off-the-shelf boost modules often suffer from poor thermal dissipation, extreme output voltage ripple (>150mV), and lack essential overvoltage/hot-plug protection.</p>
<p>I designed a dedicated, high-efficiency USB-C to 12V step-up power module delivering up to 18W (12V @ 1.5A) with industrial-grade ripple suppression and robust hot-plug surge survivability.</p>
"""),
            ("architecture", "Power Stage Selection & Inductor Sizing", """
<p>The switching regulator circuitry is calculated for high efficiency and continuous conduction:</p>
<ul>
  <li><strong>CX8823 Synchronous Boost Controller:</strong> Operates at high switching frequency (up to 1.2 MHz), reducing required passive component volume while maintaining high conversion efficiency across light to full loads.</li>
  <li><strong>3.3 µH Shielded Power Inductor:</strong> Sized to maintain continuous conduction mode (CCM) across the 5V to 12V operating window with saturation current rating exceeding 4.5A, preventing inductor core saturation under peak load transients.</li>
  <li><strong>Low-ESR Output Filtering:</strong> Combines a 470 µF low-ESR solid electrolytic capacitor with parallel 10 µF and 100 nF ceramic capacitors to suppress both fundamental switching ripple and high-frequency parasitic ringing, holding output ripple below 25 mV.</li>
</ul>
"""),
            ("design_highlights", "Surge Protection, DNP Options & Thermal Pour", """
<p>PCB layout and circuit protection highlights:</p>
<ul>
  <li><strong>Hot-Plug TVS Surge Clamping:</strong> Placed fast-response bidirectional TVS diodes (Z1 / D1) immediately adjacent to the USB-C VBUS pin to clamp inductive voltage spikes caused by cable inductance during hot-plugging.</li>
  <li><strong>DNP (Do Not Populate) Configuration:</strong> Included DNP resistor footprint options in the feedback network, enabling simple one-component configuration for alternative output voltages (9V, 15V, or 19V).</li>
  <li><strong>High-Current Thermal Layout:</strong> Minimized the high di/dt switching loop area by placing the input caps, inductor, switching IC, and output caps in a tight linear flow. Employed 2 oz copper pours with thermal vias to conduct heat away into the ground plane.</li>
</ul>
"""),
            ("results", "Load Testing & Thermal Verification", """
<p>Bench validation with electronic DC loads confirmed outstanding power density:</p>
<ul>
  <li>Measured conversion efficiency exceeding <strong>92.1%</strong> at 12V 1.0A output, maintaining over 88% efficiency at maximum 1.5A continuous output.</li>
  <li>Output ripple remained below <strong>22 mV peak-to-peak</strong> under full 18W load.</li>
  <li>Thermal equilibrium reached 58 °C under ambient room temperature without forced-air cooling.</li>
</ul>
""")
        ]
    },
    {
        "slug": "custom-stm32-pcb",
        "num": "11",
        "badge": "MCU HARDWARE / 32-BIT ARM",
        "cat_str": "pcb embedded hardware",
        "title": "Custom Mini STM32 PCB Design",
        "subtitle": "Minimalist System Board for STM32F103C8T6 ARM Cortex-M3 with Matched Crystal Oscillator, USB 2.0 Differential Routing, and SWD Debug",
        "role": "Hardware & PCB Design Engineer",
        "client": "Personal Engineering Project",
        "period": "2025",
        "stack": ["KiCad", "STM32F103", "ARM Cortex-M3", "USB 2.0", "Crystal Tank", "PCB Layout", "SWD Debug"],
        "metrics": [
            ("72 MHz", "ARM Cortex-M3"),
            ("16 MHz", "Load-Matched Crystal"),
            ("2-Layer", "Continuous GND Plane"),
            ("4-Pin", "SWD Debug Header")
        ],
        "summary": "Designed an ultra-compact minimalist microcontroller system board centered on the popular STM32F103C8T6 ARM Cortex-M3 processor (72 MHz). Overcame common clone-board flaws by engineering an optimized 2-layer PCB layout with unbroken ground return planes, calculated 16MHz crystal load capacitance, 22Ω series damping on USB 2.0 full-speed differential traces, AMS1117-3.3 power rail, and SWD debug header.",
        "cover_img": "mini-stm32-pcb-3d.gif",
        "fig1_img": "mini-stm32-pcb-layout.gif",
        "fig1_cap": "Figure 1: Two-layer PCB layout: top routing, continuous bottom ground return plane, and differential USB trace pairs.",
        "fig2_img": "mini-stm32-pcb-3d.gif",
        "fig2_cap": "Figure 2: 3D render showing compact form factor, QFP-48 breakout headers, crystal tank, and reset button.",
        "gallery_imgs": [
            ("mini-stm32-pcb-3d.gif", "3D CAD model"),
            ("mini-stm32-pcb-layout.gif", "2-layer PCB routing layout"),
            ("atmega128-dev-board-3d.png", "Dev board comparison")
        ],
        "sections": [
            ("overview", "Motivation & Design Objectives", """
<p>Generic 'Blue Pill' STM32 boards are notorious for design bugs: incorrect USB pull-up resistors (10k instead of 1.5k), misplaced crystal capacitors causing erratic PLL clock startup, and inadequate power decoupling resulting in reset loops during ADC or flash operations.</p>
<p>I engineered a clean, robust, custom STM32F103 board resolving all known reference errors to serve as a rock-solid hardware platform for my RTOS and embedded robotics projects.</p>
"""),
            ("architecture", "Crystal Load Matching & USB 2.0 Circuitry", """
<p>Key schematic calculations and layout implementations:</p>
<ul>
  <li><strong>16 MHz Crystal Oscillator Tank:</strong> Calculated exact load capacitor values \(C_L = (C_1 \times C_2) / (C_1 + C_2) + C_{stray}\) for a 16 pF crystal, using 20 pF COG/NPO ceramic caps. Routed crystal traces symmetrically with an isolating ground shield to guarantee jitter-free PLL multiplication up to 72 MHz.</li>
  <li><strong>USB 2.0 Compliance:</strong> Implemented a precision 1.5 kΩ pull-up resistor to 3.3V on the USB D+ line to signal Full-Speed (12 Mbps) device enumeration to the host PC. Inserted 22 Ω series damping resistors to match driver impedance and eliminate ringing.</li>
  <li><strong>Power Supply Decoupling:</strong> Placed 100 nF ceramic decoupling capacitors directly under each of the four VDD/VSS pin pairs with direct via connections to the solid bottom ground plane.</li>
</ul>
"""),
            ("design_highlights", "SWD Debug Interface & Ergonomic Layout", """
<p>Hardware layout decisions executed in KiCad:</p>
<ul>
  <li><strong>SWD Debug Port:</strong> Dedicated 4-pin right-angle header (3.3V, SWDIO, SWCLK, GND) for fast debugging via ST-Link V2 and Segger J-Link with hardware breakpoint support.</li>
  <li><strong>Dual Breadboard Header:</strong> All 32 usable GPIOs brought out to dual standard 0.1-inch pitch headers with pinouts labeled clearly on silkscreen.</li>
  <li><strong>Bootloader Selector:</strong> Tactile jumpers for BOOT0 / BOOT1 selection allowing instant switching between flash execution and internal system memory UART bootloader.</li>
</ul>
"""),
            ("results", "Validation & Firmware Benchmarks", """
<p>Board testing confirmed full electrical compliance:</p>
<ul>
  <li>Clean USB Virtual COM Port (VCP) and HID enumeration across Windows and Linux without dropped packets.</li>
  <li>PLL startup time under 1.2 ms with zero clock jitter or oscillator stall across -20 °C to +70 °C thermal stress.</li>
  <li>Flawless FreeRTOS execution running 8 concurrent tasks with zero power rail dropouts.</li>
</ul>
""")
        ]
    },
    {
        "slug": "hourglass-atmega328p-pcb",
        "num": "12",
        "badge": "HARDWARE / SHIFT REGISTERS / SPI",
        "cat_str": "pcb embedded hardware",
        "title": "Custom Hourglass PCB with ATmega8A",
        "subtitle": "Two-Board Stacked Electronic Sand Timer with 29 Blue LEDs, 4x 74HC595 SPI Shift Registers, Dual Tilt Switches, and Multi-Duration Selection",
        "role": "Analog & Embedded Circuit Designer",
        "client": "Novelty Hardware / Embedded Prototype",
        "period": "2025",
        "stack": ["KiCad", "ATmega8A", "74HC595", "SPI", "SW-200D", "TP4056", "AMS1117", "MiniCore"],
        "metrics": [
            ("29 LEDs", "Triangular Arrays"),
            ("4x 74HC595", "Cascaded SPI"),
            ("1 / 5 / 10 min", "Timer Durations"),
            ("Dual Board", "Interconnected Stack")
        ],
        "summary": "Designed a two-board, hourglass-shaped electronic sand timer driven by an ATmega8A microcontroller. Controls 29 high-brightness blue LEDs arranged in opposing triangular sand chambers through a cascaded chain of four 74HC595 shift registers over hardware SPI. Dual SW-200D tilt ball switches detect board inversion, triggering gravity-accurate falling sand animations, selectable 1/5/10-minute intervals, and active buzzer alarms.",
        "cover_img": "hourglass-schematic.gif",
        "fig1_img": "hourglass-schematic.gif",
        "fig1_cap": "Figure 1: Complete circuit schematic: ATmega8A MCU, four 74HC595 shift registers in SPI cascade, dual SW-200D tilt switches, and TP4056 LiPo charger.",
        "fig2_img": "hourglass-schematic.gif",
        "fig2_cap": "Figure 2: Pin mapping, shift register bit allocation table, and state machine transition flow (Idle, Running, Sparkle, Alarm).",
        "gallery_imgs": [
            ("hourglass-schematic.gif", "Circuit schematic & bit allocation"),
            ("mini-stm32-pcb-3d.gif", "Hardware layout reference"),
            ("atmega128-dev-board-3d.png", "PCB manufacturing comparison")
        ],
        "sections": [
            ("overview", "Project Concept & Mechanical Geometry", """
<p>Traditional mechanical sand timers are aesthetically captivating but lack precision, duration flexibility, and audio alerts. The goal was to design an electronic hourglass PCB that replicates the physics of flowing sand grains using an animated LED matrix in a novel hourglass-shaped board contour.</p>
<p>The design utilizes a two-board stacked architecture: the front board displays the 29-LED sand matrix and orientation tilt switches, while the rear board houses the ATmega8A controller, duration selection buttons, buzzer alarm, and LiPo charging circuitry.</p>
"""),
            ("architecture", "Cascaded 74HC595 SPI Matrix & Shared Waist LED", """
<p>Driving 29 LEDs with an ATmega8A (DIP-28) without exhausting IO lines required an optimized multiplexing architecture:</p>
<ul>
  <li><strong>Cascaded Shift Register Chain:</strong> Connected four 8-bit <strong>74HC595</strong> shift registers in a daisy chain using just three microcontroller pins (SPI MOSI, SCK, and Latch). This yields 32 controllable digital outputs, with 29 allocated to LEDs and 3 for expansion.</li>
  <li><strong>Shared Center Waist LED:</strong> In Version 4.0, the two center LEDs from earlier prototypes were merged into a single shared LED located exactly at the hourglass waist. This represents the bottleneck through which sand grains fall, and reduced the required inter-board connector from 8 to 7 pins.</li>
  <li><strong>Dual SW-200D Tilt Switches:</strong> Two ball tilt switches mounted at 45-degree opposing angles detect physical board inversion, triggering a reverse-gravity sand flow sequence.</li>
</ul>
"""),
            ("design_highlights", "Power Management & State Machine Firmware", """
<p>Circuit design and firmware state sequencer:</p>
<ul>
  <li><strong>Power Supply & Battery Charging:</strong> Powered by a rechargeable 3.7V LiPo battery managed by an onboard <strong>TP4056</strong> linear charger with micro-USB input, stepped down to a steady 3.3V logic rail via an AMS1117-3.3 regulator.</li>
  <li><strong>Selectable Durations:</strong> Three tactile buttons on the back PCB allow users to select 1-minute, 5-minute, or 10-minute timer intervals, confirmed with distinct audio chirps from an active buzzer.</li>
  <li><strong>Animation State Machine:</strong> The ATmega8A firmware (programmed via ISP using MiniCore) implements a non-blocking state machine with four operational phases: <em>Idle Breathing</em>, <em>Running Sand Flow</em> with pseudo-random grain drops, <em>Done Sparkle</em> animation, and <em>Buzzer Alarm</em>.</li>
</ul>
"""),
            ("results", "Visual Flow & Electrical Validation", """
<p>Validation across breadboard and initial board fabrication:</p>
<ul>
  <li>Achieved smooth 60 Hz LED refresh rates over hardware SPI with zero visible flicker or brightness variance.</li>
  <li>Accurate timing countdown within 0.5 seconds of nominal time across 1, 5, and 10-minute cycles.</li>
  <li>Current consumption during sleep mode measured under 15 µA, enabling months of standby battery shelf life.</li>
</ul>
""")
        ]
    },
    {
        "slug": "mini-logic-analyzer",
        "num": "13",
        "badge": "INSTRUMENTATION / DMA / DAQ",
        "cat_str": "embedded hardware",
        "title": "Mini Logic Analyzer (8-Channel 24MHz DMA DAQ)",
        "subtitle": "High-Speed 8-Channel Digital Logic Analyzer on STM32 ARM Cortex-M4 with Hardware Timer DMA Capture, Circular SRAM Buffering, and Sigrok/PulseView Export",
        "role": "Embedded Systems & Firmware Engineer",
        "client": "Test & Measurement Tooling",
        "period": "2025",
        "stack": ["STM32F4", "ARM Cortex-M4", "DMA", "Hardware Timers", "Sigrok", "PulseView", "USB VCP"],
        "metrics": [
            ("24 MHz", "Parallel Sample Rate"),
            ("8 Channels", "Simultaneous Digital Inputs"),
            ("3.3V / 5V", "Tolerant Inputs"),
            ("100%", "Sigrok Compatible")
        ],
        "summary": "Built a pocket-sized, high-speed 8-channel digital logic analyzer leveraging the DMA and hardware timer architecture of an STM32 ARM Cortex-M4 microcontroller. Streams digital logic captures at sampling rates up to 24MHz across 8 parallel GPIO pins using double-buffered circular SRAM acquisition, streaming packets over USB Virtual COM Port (VCP) to the open-source Sigrok / PulseView protocol analyzer suite.",
        "cover_img": "bridge-faulty-sensor.gif",
        "fig1_img": "bridge-faulty-sensor.gif",
        "fig1_cap": "Figure 1: Real-time digital waveform acquisition in PulseView: decoding I2C and high-speed SPI bus packets captured at 24MHz.",
        "fig2_img": "bridge-faulty-sensor.gif",
        "fig2_cap": "Figure 2: Double-buffered DMA capture engine and trigger detection state machine.",
        "gallery_imgs": [
            ("bridge-faulty-sensor.gif", "PulseView waveform decode"),
            ("mini-stm32-pcb-3d.gif", "Controller board reference"),
            ("atmega128-dev-board-3d.png", "Hardware DAQ form factor")
        ],
        "sections": [
            ("overview", "Project Motivation & Instrumentation Needs", """
<p>Debugging high-speed digital communication protocols (SPI, I2C, UART, 1-Wire) in embedded systems projects requires a logic analyzer. Commercial instruments like Saleae are expensive, while cheap clone analyzers often suffer from flaky USB drivers and unbuffered packet loss.</p>
<p>I engineered a dedicated, low-cost 8-channel logic analyzer using the high-performance DMA (Direct Memory Access) architecture of the STM32 microcontroller, capturing clean digital traces with zero CPU overhead.</p>
"""),
            ("architecture", "Timer-Triggered DMA Parallel Capture Pipeline", """
<p>The core acquisition engine operates entirely in hardware without CPU cycle consumption:</p>
<ul>
  <li><strong>Parallel GPIO Port Sampling:</strong> Grouped 8 input pins on GPIO Port A (pins 0 through 7). A hardware Timer (TIM1/TIM2) generates precise clock triggers up to 24 MHz.</li>
  <li><strong>Circular DMA Streaming:</strong> Each timer event triggers a DMA request that transfers the entire 8-bit GPIO input data register (IDR) directly into a circular SRAM double-buffer. While DMA fills Buffer A, the USB peripheral transmits Buffer B to the host computer, eliminating sample dropouts.</li>
  <li><strong>Input Clamping & 5V Tolerance:</strong> Inserted 100 Ω current-limiting series damping resistors and Schottky clamping diodes on each channel, allowing safe connection to both 3.3V and 5V logic buses without damaging the STM32 pins.</li>
</ul>
"""),
            ("design_highlights", "Sigrok / PulseView Protocol Compatibility", """
<p>Host software integration and trigger firmware:</p>
<ul>
  <li><strong>Standard Protocol Emulation:</strong> The STM32 USB Virtual COM Port implements the standard Openbench Logic Sniffer (OLS) / Sump protocol. This allows immediate plug-and-play compatibility with <strong>Sigrok</strong> and <strong>PulseView</strong> without custom device drivers.</li>
  <li><strong>Hardware Edge Triggering:</strong> Configured flexible pre-trigger and post-trigger ring buffering. The analyzer captures continuous data and freezes the buffer upon detecting rising, falling, or pattern matching triggers.</li>
  <li><strong>Zero CPU Overhead:</strong> By offloading both pin acquisition and USB transmission to DMA channels, the Cortex-M4 CPU remains virtually idle during full 24MHz data acquisition.</li>
</ul>
"""),
            ("results", "Protocol Decoding & Acquisition Accuracy", """
<p>Bench validation against high-speed digital buses:</p>
<ul>
  <li>Successfully captured and decoded 12 MHz SPI bus communications with zero bit errors or frame dropouts.</li>
  <li>Accurately decoded I2C bus transactions, UART packets up to 3 Mbaud, and PWM signals with sub-42 nanosecond timing resolution.</li>
  <li>Cost less than $8 to build while matching functionality of entry-level commercial analyzers.</li>
</ul>
""")
        ]
    },
    {
        "slug": "sap-flow-sensor",
        "num": "14",
        "badge": "ANALOG FRONT-END / AGRI-TECH",
        "cat_str": "embedded pcb",
        "title": "Plant Sap Flow Sensor",
        "subtitle": "Precision Agro-Forestry Instrumentation with Low-Noise Analog Front-End, Thermocouple Probes, and Custom Data-Acquisition Transpiration Formula",
        "role": "Analog Instrumentation & Embedded Engineer",
        "client": "Agronomic Research / ITB",
        "period": "2025",
        "stack": ["Analog Front-End", "Thermocouples", "Op-Amps", "Granier Method", "KiCad", "SolidWorks", "SLA 3D"],
        "metrics": [
            ("0.02 °C", "Thermal Resolution"),
            ("Granier", "TDM Methodology"),
            ("SLA 3D", "Weatherproof Enclosure"),
            ("Low Noise", "Instrumentation Amp")
        ],
        "summary": "Engineered a plant sap flow sensor instrument designed to track plant transpiration and water consumption in real time. Designed a high-precision low-noise analog front-end (AFE) conditioning microvolt-level thermocouple probe signals based on the Granier thermal dissipation method (TDM), paired with a customized mathematical DAQ calculation algorithm and a water-resistant 3D modeled tree-mounting enclosure.",
        "cover_img": "sap-flow-probes.jpg",
        "fig1_img": "sap-flow-board.gif",
        "fig1_cap": "Figure 1: Custom analog instrumentation board showing low-noise op-amp filtering, thermocouple connectors, and MCU header.",
        "fig2_img": "sap-flow-probes.jpg",
        "fig2_cap": "Figure 2: Physical stainless-steel needle thermocouple probes inserted into tree xylem tissue for thermal dissipation tracking.",
        "gallery_imgs": [
            ("sap-flow-probes.jpg", "Thermocouple probe needles"),
            ("sap-flow-board.gif", "Analog conditioning PCB"),
            ("wire-harness-top.jpg", "Field wiring reference")
        ],
        "sections": [
            ("overview", "Agronomic Context & Measurement Physics", """
<p>Monitoring sap flow rate in tree xylem vessels provides direct, quantitative data on plant water stress, transpiration dynamics, and irrigation efficiency. The Granier Thermal Dissipation Method (TDM) uses two needle probes inserted radially into the tree trunk: an upper heated probe and a lower unheated reference probe.</p>
<p>As water moves through the xylem, heat is carried away; the temperature differential (\(\Delta T\)) between the two probes is inversely proportional to sap flux density. Measuring microvolt thermocouple outputs reliably under outdoor agricultural conditions requires extreme analog precision.</p>
"""),
            ("architecture", "Low-Noise Analog Front-End (AFE) Design", """
<p>The sensor circuit conditions delicate thermoelectric signals:</p>
<ul>
  <li><strong>Instrumentation Amplifier Front-End:</strong> Integrated low-offset, low-drift rail-to-rail instrumentation amplifiers providing 110 dB+ Common-Mode Rejection Ratio (CMRR) to eliminate 50Hz mains hum and environmental RF pickup.</li>
  <li><strong>Precision Cold-Junction Compensation:</strong> Implemented local RTD/thermistor temperature sensing at the thermocouple connector terminal block to ensure sub-0.05°C temperature differential accuracy.</li>
  <li><strong>Constant-Current Heater Driver:</strong> Designed a regulated low-noise constant-current source driving the upper heating needle with 0.2W continuous dissipation, preventing thermal runaway or measurement drift.</li>
</ul>
"""),
            ("design_highlights", "Custom DAQ Formula & Weatherproof Enclosure", """
<p>Firmware calculation and mechanical mounting:</p>
<ul>
  <li><strong>Empirical Flow Velocity Equation:</strong> Implemented the Granier empirical calibration formula \(u = 0.0119 \times K^{1.231}\) (where \(K = (\Delta T_{max} - \Delta T) / \Delta T\)) directly inside the microcontroller firmware, computing sap flux in liters per hour per square meter.</li>
  <li><strong>3D SLA Enclosure Design:</strong> Modeled a customized UV-resistant enclosure in SolidWorks, manufactured using SLA resin printing. Features silicone gaskets, conformal cable glands, and tree-trunk curved mounting wings for stable attachment.</li>
</ul>
"""),
            ("results", "Field Testing & Transpiration Tracking", """
<p>Field deployment on experimental crops confirmed high sensitivity:</p>
<ul>
  <li>Detected sharp diurnal transpiration curves matching sunrise and solar irradiance peaks with under 15-minute response lag.</li>
  <li>Temperature differential measurement stability achieved <strong>±0.02 °C</strong> resolution across outdoor temperature fluctuations from 20 °C to 38 °C.</li>
  <li>Validated reliable low-power battery operation suitable for solar-assisted remote agro-forestry monitoring.</li>
</ul>
""")
        ]
    },
    {
        "slug": "soccer-robot-ep-lab",
        "num": "15",
        "badge": "ROBOTICS / MECHATRONICS / IOT",
        "cat_str": "embedded software",
        "title": "Soccer Robot (Engineering Physics Lab II)",
        "subtitle": "3-Wheel Holonomic Omni-Directional Mobile Robot with SolidWorks Chassis, Kotlin Android Wi-Fi Teleoperation, and Closed-Loop C++ Firmware",
        "role": "Lead Systems Integration & Embedded Engineer",
        "client": "Engineering Physics Laboratory II / ITB",
        "period": "2025",
        "stack": ["C++", "Arduino", "Kotlin", "Android Studio", "SolidWorks", "Omni-Wheels", "Wi-Fi UDP", "PID Control"],
        "metrics": [
            ("3-Wheel", "Holonomic Drive"),
            ("< 20 ms", "Wi-Fi Command Latency"),
            ("360 deg", "Vector Agility"),
            ("SolidWorks", "Chassis Design")
        ],
        "summary": "Designed, fabricated, and integrated an agile 3-wheel holonomic omni-drive mobile soccer robot for the Engineering Physics Laboratory competition. Modeled the lightweight chassis in SolidWorks, developed a custom Kotlin Android app featuring multi-touch virtual joysticks and Wi-Fi UDP command streaming, and wrote the microcontroller C++ firmware for inverse kinematics, closed-loop wheel speed PID control, and dribbler actuation.",
        "cover_img": "soccer-robot-3d.gif",
        "fig1_img": "soccer-robot-android.gif",
        "fig1_cap": "Figure 1: Custom Kotlin Android Studio teleoperation interface: dual virtual thumbstick and Wi-Fi UDP packet monitor.",
        "fig2_img": "soccer-robot-3d.gif",
        "fig2_cap": "Figure 2: SolidWorks 3D mechanical model: 120-degree omni-wheel geometry, low-CG battery tray, and kicker solenoid bracket.",
        "gallery_imgs": [
            ("soccer-robot-3d.gif", "3D CAD chassis model"),
            ("soccer-robot-android.gif", "Android Kotlin control app"),
            ("drone-airframe-3d.gif", "Mechanical design reference")
        ],
        "sections": [
            ("overview", "Project Challenge & Leadership Role", """
<p>The Engineering Physics Laboratory II soccer competition challenged student teams to design an autonomous or teleoperated mobile robot capable of aggressive acceleration, omnidirectional strafing, and ball control in a competitive field environment.</p>
<p>I took the initiative as team lead for system integration—bridging mechanical CAD design, wireless mobile app development, and embedded motor firmware into a cohesive, responsive robotic platform.</p>
"""),
            ("architecture", "Holonomic Inverse Kinematics & Motor Control", """
<p>The mathematical and firmware foundations of the robot:</p>
<ul>
  <li><strong>3-Wheel Omni-Drive Kinematics:</strong> Placed three omnidirectional wheels spaced 120 degrees apart. The firmware computes wheel velocity vectors via inverse kinematics: \([v_1, v_2, v_3]^T = M \cdot [v_x, v_y, \omega]^T\), enabling simultaneous translation and rotation in any direction without turning the chassis.</li>
  <li><strong>Closed-Loop Velocity Regulation:</strong> Dual quadrature encoders on each DC gearmotor feed high-frequency timer interrupts, with C++ PID loops stabilizing wheel speeds despite carpet friction changes.</li>
  <li><strong>Active Dribbler & Kicker:</strong> An auxiliary high-RPM brushless roller traps the ball against the chassis frame while a spring-loaded solenoid mechanism executes targeted kicks.</li>
</ul>
"""),
            ("design_highlights", "Kotlin Android App & SolidWorks Mechanical CAD", """
<p>Integration between user experience and physical hardware:</p>
<ul>
  <li><strong>Low-Latency UDP Telemetry App:</strong> Developed a native Android application in Kotlin using Android Studio. Features dual virtual joysticks, transmission rate configuration (up to 50 Hz), and packet checksum validation over Wi-Fi UDP sockets.</li>
  <li><strong>SolidWorks Lightweight Chassis:</strong> Designed a multi-tier acrylic and aluminum plate chassis with a low center of gravity to prevent rollover during rapid acceleration reversals. Incorporated modular battery bays and motor brackets.</li>
</ul>
"""),
            ("results", "Competition Agility & Responsiveness", """
<p>Competitive performance on the arena court:</p>
<ul>
  <li>Achieved sub-20 ms end-to-end command latency from mobile touchscreen input to motor shaft acceleration.</li>
  <li>Demonstrated continuous 360-degree vector strafing at speeds up to 1.6 m/s with tight trajectory control.</li>
  <li>Recognized for superior maneuverability and system integration finish in the lab cohort.</li>
</ul>
""")
        ]
    },
    {
        "slug": "iiot-motor-control-system",
        "num": "16",
        "badge": "IIOT / SCADA / CLOUD",
        "cat_str": "iiot software",
        "title": "IIoT Capstone Motor Control & Cloud SCADA",
        "subtitle": "Industrial Automation Cell with Omron PLC, Weintek HMI, Node-RED Edge Gateway, Next.js Web Dashboard, and MongoDB Historical Telemetry",
        "role": "Lead IoT & Industrial Automation Engineer",
        "client": "Industrial Capstone Project",
        "period": "2025",
        "stack": ["Omron PLC", "Weintek HMI", "Node-RED", "Next.js", "MongoDB", "Modbus RTU/TCP", "MQTT", "CX-Designer"],
        "metrics": [
            ("5 Layers", "IIoT Stack"),
            ("Modbus", "PLC Protocol"),
            ("Real-Time", "MQTT Streaming"),
            ("Next.js", "Cloud SCADA")
        ],
        "summary": "Engineered an end-to-end industrial motor control and supervisory platform spanning factory-floor PLC hardware to cloud analytics. Programmed an Omron CP1E PLC with ladder logic for three-phase motor sequencing and safety interlocks, designed an operator touchscreen interface on a Weintek cMT series HMI, integrated a Node-RED edge gateway over Modbus TCP/RTU, and built a Next.js web portal logging time-series motor telemetry to MongoDB.",
        "cover_img": "iiot-weintek-screen.jpg",
        "fig1_img": "iiot-weintek-screen.jpg",
        "fig1_cap": "Figure 1: Weintek industrial touch HMI screen: motor RPM, current draw, thermal trend graphs, and manual override controls.",
        "fig2_img": "iiot-nextjs-cloud.jpg",
        "fig2_cap": "Figure 2: Next.js cloud SCADA dashboard: live telemetry charts, alarm logging, and historical motor performance analytics.",
        "gallery_imgs": [
            ("iiot-weintek-screen.jpg", "Weintek HMI screen"),
            ("iiot-nextjs-cloud.jpg", "Next.js cloud portal"),
            ("microhydro-telelab-control.gif", "SCADA architecture reference")
        ],
        "sections": [
            ("overview", "Industrial Scope & Plant Architecture", """
<p>Modern Industry 4.0 factories require bridging rugged operational technology (OT) on the shop floor with flexible information technology (IT) in the cloud. Motors and drives must not only be controlled with deterministic safety interlocks but also monitored continuously for predictive maintenance.</p>
<p>I architected and deployed a multi-tier IIoT motor control platform connecting factory-floor PLCs to a cloud-accessible supervisory dashboard with real-time analytics.</p>
"""),
            ("architecture", "5-Tier Edge-to-Cloud Communication Pipeline", """
<p>The system spans five integrated industrial layers:</p>
<ul>
  <li><strong>Level 0/1 (Field & Control):</strong> An <strong>Omron CP1E</strong> PLC executing deterministic Ladder Logic manages motor contactors, soft-starters, emergency stop chains, and inductive speed sensors.</li>
  <li><strong>Level 2 (Local Supervisory):</strong> A <strong>Weintek cMT</strong> touch HMI communicates with the PLC via RS-485 Modbus RTU, rendering high-contrast ISA-101 screens for operator control.</li>
  <li><strong>Level 3 (Edge Gateway):</strong> A Linux edge computer running <strong>Node-RED</strong> polls Modbus TCP/RTU registers at 2 Hz, packages motor health metrics (RPM, current, temperature, running hours) into JSON payloads, and publishes them over encrypted MQTT.</li>
  <li><strong>Level 4/5 (Cloud SCADA & Database):</strong> A custom <strong>Next.js</strong> web application subscribes to MQTT topics via WebSockets, rendering live SVG telemetry widgets and persisting historical time-series records to a <strong>MongoDB</strong> database for analytics.</li>
</ul>
"""),
            ("design_highlights", "Safety Interlocks & Modbus Mapping", """
<p>Key automation and software engineering decisions:</p>
<ul>
  <li><strong>Hardware & Software Fail-Safes:</strong> Implemented hardware E-stop circuits backed by software watchdog heartbeat registers. Loss of edge communication halts motor commands and locks controls in a safe idle state.</li>
  <li><strong>Comprehensive Modbus Register Map:</strong> Created structured 16-bit holding register mappings across the PLC, HMI, and Node-RED gateway, standardizing float-to-integer conversions and bitmasked alarm flags.</li>
  <li><strong>Role-Based Web Access:</strong> Built secure operator and administrator authentication in Next.js, allowing remote monitoring while restricting motor actuation commands to verified local personnel.</li>
</ul>
"""),
            ("results", "Operational Reliability & Real-Time Metrics", """
<p>Bench and prototype validation confirmed industrial reliability:</p>
<ul>
  <li>Sub-200 ms end-to-end telemetry propagation latency from PLC register change to cloud browser update.</li>
  <li>Zero data loss during simulated network disconnects thanks to Node-RED local buffer queuing.</li>
  <li>Intuitive UI reduced simulated operator alarm diagnosis time by over 50%.</li>
</ul>
""")
        ]
    },
    {
        "slug": "micro-hydro-hmi-system",
        "num": "17",
        "badge": "INDUSTRIAL HMI / SCADA / DAQ",
        "cat_str": "iiot embedded",
        "title": "MicroHydroPower TeleLab & Aeroponic HMI System",
        "subtitle": "Remote Educational SCADA Platform for Micro-Hydro Turbines and Aeroponic Monitoring with High-Performance ISA-101 HMI and FreeRTOS DAQ",
        "role": "Lead IoT, HMI & Embedded Systems Engineer",
        "client": "Renewable Energy Laboratory / ITB",
        "period": "2025",
        "stack": ["ISA-101 HMI", "FreeRTOS", "Node-RED", "MQTT", "MySQL", "CX-Designer", "Sensors"],
        "metrics": [
            ("ISA-101", "HMI Standard"),
            ("FreeRTOS", "Embedded DAQ"),
            ("MySQL", "Historical Logging"),
            ("Remote", "TeleLab Access")
        ],
        "summary": "Designed and deployed a remote laboratory tele-operation and supervisory system for a micro-hydro electric power generator and companion aeroponic greenhouse. Developed high-performance ISA-101 compliant HMI screens in CX-Designer / Weintek, an embedded FreeRTOS data acquisition sensor hub measuring water pressure, turbine RPM, and power output, and a Node-RED MQTT telemetry bridge logging into MySQL.",
        "cover_img": "microhydro-telelab-control.gif",
        "fig1_img": "microhydro-telelab-control.gif",
        "fig1_cap": "Figure 1: ISA-101 compliant HMI control panel: turbine flow regulation, valve positioning, generator electrical output, and alarm indicators.",
        "fig2_img": "microhydro-telelab-overview.gif",
        "fig2_cap": "Figure 2: MicroHydroPower telelab system overview showing hydraulic piping, turbine alternator, aeroponic misting bays, and sensor nodes.",
        "gallery_imgs": [
            ("microhydro-telelab-control.gif", "HMI turbine control screen"),
            ("microhydro-telelab-overview.gif", "System schematic & overview"),
            ("iiot-weintek-screen.jpg", "Industrial HMI layout")
        ],
        "sections": [
            ("overview", "TeleLab Educational Mission & Scope", """
<p>Practical laboratory education in renewable energy systems is often constrained by physical access limits, safety hazards around high-pressure hydraulic turbines, and geographical barriers for remote students. The MicroHydroPower TeleLab was created to give students real-time interactive control and telemetry over a physical hydro-turbine and aeroponic test rig from any web browser.</p>
<p>I was responsible for developing the industrial human-machine interface (HMI), the embedded sensor DAQ node, and the telemetry logging infrastructure.</p>
"""),
            ("architecture", "ISA-101 High-Performance HMI Design", """
<p>Rather than flashy, distracting graphics, the user interface follows the <strong>ISA-101 High-Performance HMI</strong> industrial standard:</p>
<ul>
  <li><strong>Muted Color Palette:</strong> Gray backgrounds with high-contrast monochrome indicators minimize operator eye fatigue; bright colors (orange, red, yellow) are reserved strictly for alarm and out-of-spec conditions.</li>
  <li><strong>Analog Visual Context:</strong> Implemented analog trend meters with embedded normal-operating-range bands, allowing operators to diagnose whether turbine head pressure or generator frequency is drifting before threshold alarms trip.</li>
  <li><strong>Comprehensive Telemetry:</strong> Live metrics include water flow rate (L/min), turbine shaft RPM, generator terminal voltage, AC frequency (50 Hz grid target), electrical power output (W), and aeroponic root-zone humidity.</li>
</ul>
"""),
            ("design_highlights", "FreeRTOS DAQ Hub & Database Logging", """
<p>Embedded instrumentation and data persistence:</p>
<ul>
  <li><strong>FreeRTOS Sensor Hub:</strong> Built an embedded sensor acquisition node sampling pressure transducers, optical shaft tachometers, and hall-effect current sensors using FreeRTOS timer tasks with anti-aliasing digital filtering.</li>
  <li><strong>MQTT Telemetry Gateway:</strong> An edge Node-RED gateway packages sensor data into structured MQTT topics published to an access-controlled broker.</li>
  <li><strong>Relational MySQL Logging:</strong> Ingests all telemetry points into an indexed MySQL database, enabling students to download CSV datasets for computational fluid dynamics (CFD) and turbine efficiency curve analysis.</li>
</ul>
"""),
            ("results", "Pedagogical Impact & System Uptime", """
<p>Successful deployment in academic laboratory courses:</p>
<ul>
  <li>Enabled over 100 undergraduate students to conduct live hydro-turbine efficiency experiments remotely with zero hardware safety incidents.</li>
  <li>Maintained 99.8% server and telemetry uptime across semester-long laboratory coursework.</li>
  <li>Recognized for outstanding clarity and usability in human factors engineering.</li>
</ul>
""")
        ]
    },
    {
        "slug": "tinyml-motor-anomaly",
        "num": "18",
        "badge": "TINYML / EDGE AI / DSP",
        "cat_str": "embedded software",
        "title": "TinyML Machine Vibration Anomaly Detection",
        "subtitle": "Edge Machine Learning Condition Monitoring on ESP32-S3 with 512-Point FFT Feature Extraction and Deep Autoencoder Anomaly Classification",
        "role": "Lead Embedded AI & DSP Engineer",
        "client": "Predictive Maintenance Prototype",
        "period": "2025",
        "stack": ["TinyML", "ESP32-S3", "Edge Impulse", "Python", "TensorFlow Lite", "512-FFT", "C++", "Vibration Analysis"],
        "metrics": [
            ("512-Point", "Real-Time FFT"),
            ("< 12 ms", "Inference Latency"),
            ("97.6%", "Anomaly Precision"),
            ("15 µA", "Deep Sleep Current")
        ],
        "summary": "Engineered an edge AI vibration anomaly detection node for industrial rotating machinery centered on the ESP32-S3 microcontroller. Samples a 3-axis digital accelerometer at 1.6kHz, executes on-device 512-point Fast Fourier Transform (FFT) spectral feature extraction, and feeds frequency-domain power bands into an optimized Deep Autoencoder neural network (TensorFlow Lite for Microcontrollers), flagging bearing faults when reconstruction error exceeds 3-sigma thresholds.",
        "cover_img": "tinyml-anomaly.gif",
        "fig1_img": "tinyml-anomaly.gif",
        "fig1_cap": "Figure 1: Edge Impulse spectral feature extraction: 512-point FFT vibration spectrogram showing distinct bearing inner-race fault frequencies.",
        "fig2_img": "tinyml-anomaly.gif",
        "fig2_cap": "Figure 2: Real-time anomaly score clustering and reconstruction error tracking against statistical threshold.",
        "gallery_imgs": [
            ("tinyml-anomaly.gif", "FFT spectrum and anomaly clustering"),
            ("microhydro-telelab-control.gif", "Industrial motor monitoring"),
            ("mini-stm32-pcb-3d.gif", "Embedded sensor reference")
        ],
        "sections": [
            ("overview", "Predictive Maintenance & Edge AI Motivation", """
<p>Bearing failure is the leading cause of catastrophic motor breakdowns in industrial manufacturing. Traditional periodic maintenance is either wasteful (replacing healthy bearings) or reactionary (replacing them after catastrophic seizure). While streaming raw 3-axis vibration data continuously to the cloud incurs immense bandwidth and cellular data costs, deploying TinyML on edge sensors solves both problems.</p>
<p>I engineered an autonomous, battery-operated vibration sensor node that analyzes motor vibrations locally on the microcontroller and only wakes up or sends alerts when early-stage bearing degradation is detected.</p>
"""),
            ("architecture", "DSP Spectral Extraction & Autoencoder Neural Network", """
<p>The on-device machine learning pipeline consists of two stages:</p>
<ul>
  <li><strong>Digital Signal Processing (512-Point FFT):</strong> Samples a high-bandwidth digital accelerometer over SPI at 1,600 Hz. The ESP32-S3 executes an optimized 512-point Fast Fourier Transform (FFT) using Xtensa DSP SIMD instructions, extracting spectral power densities across critical mechanical fault bands (ball pass frequency outer race, inner race, and cage frequency).</li>
  <li><strong>Unsupervised Autoencoder Architecture:</strong> An Autoencoder neural network was trained in Python / TensorFlow exclusively on normal motor operating vibrations. The network compresses the 64 spectral features down to an 8-dimension bottleneck layer before reconstructing them.</li>
  <li><strong>Reconstruction Error Anomaly Metric:</strong> When a mechanical defect develops (pitting, spalling, loose mounting), the novel spectral peaks cannot be accurately reconstructed; the Mean Squared Error (MSE) surges past an empirical 3-sigma statistical threshold, triggering an immediate anomaly alert.</li>
</ul>
"""),
            ("design_highlights", "TensorFlow Lite Micro C++ Deployment", """
<p>Embedded optimization techniques executed on the ESP32-S3:</p>
<ul>
  <li><strong>INT8 Quantization & Vector Acceleration:</strong> Quantized all model weights from FP32 to INT8, utilizing ESP32-S3 vector instructions to reduce model size to just 14 KB Flash and achieve inference times under 12 milliseconds.</li>
  <li><strong>Ultra-Low Power Duty Cycling:</strong> The node rests in ultra-low-power deep sleep (consuming just 15 µA) for 10 minutes, wakes up via internal timer to capture a 2-second vibration burst, executes inference, and immediately returns to sleep if normal.</li>
  <li><strong>Local BLE Diagnostics:</strong> Provides Bluetooth Low Energy beacon broadcasting for technicians walking by with a smartphone, showing instant bearing health indices without physical cable attachment.</li>
</ul>
"""),
            ("results", "Fault Detection Precision & Bench Validation", """
<p>Validation on bench motor test rigs with seeded defects:</p>
<ul>
  <li>Achieved <strong>97.6% true-positive anomaly detection</strong> on early-stage bearing inner race and outer race faults well before audible noise was noticeable.</li>
  <li>Zero false alarms observed across 200 hours of nominal motor running cycles under varying load conditions.</li>
  <li>Calculated battery lifetime exceeding <strong>18 months</strong> on a single standard 18650 Li-ion cell.</li>
</ul>
""")
        ]
    }
]

print(f"Total projects to build: {len(PROJECTS)}")

# Template generator for project detail pages
def generate_project_detail_html(proj, prev_proj, next_proj):
    slug = proj["slug"]
    num = proj["num"]
    badge = proj["badge"]
    title = proj["title"]
    subtitle = proj["subtitle"]
    role = proj["role"]
    client = proj["client"]
    period = proj["period"]
    stack = proj["stack"]
    metrics = proj["metrics"]
    summary = proj["summary"]
    cover_img = proj["cover_img"]
    fig1_img = proj["fig1_img"]
    fig1_cap = proj["fig1_cap"]
    fig2_img = proj["fig2_img"]
    fig2_cap = proj["fig2_cap"]
    gallery_imgs = proj["gallery_imgs"]
    sections = proj["sections"]
    
    prev_link = f"{prev_proj['slug']}.html"
    next_link = f"{next_proj['slug']}.html"
    prev_title = prev_proj['title']
    next_title = next_proj['title']
    
    metrics_html = "".join([f"""
        <div class="metric">
          <div class="n">{val}</div>
          <div class="lbl">{lbl}</div>
        </div>""" for val, lbl in metrics])
        
    toc_html = "".join([f"""
        <li><a href="#{sec_id}"><span class="num">{idx+1:02d}</span><span>{sec_title}</span></a></li>""" 
        for idx, (sec_id, sec_title, _) in enumerate(sections)])
        
    chips_html = "".join([f'<span class="t">{t}</span>' for t in stack])
    
    sections_body_html = ""
    for idx, (sec_id, sec_title, sec_content) in enumerate(sections):
        sections_body_html += f"""
      <section id="{sec_id}">
        <h2><span class="num">{idx+1:02d}</span>{sec_title}</h2>
        {sec_content}
      </section>
"""
        if idx == 0 and fig1_img:
            sections_body_html += f"""
      <div class="figure">
        <div class="frame">
          <img src="../uploads/projects/{fig1_img}" alt="{fig1_cap}" loading="lazy" />
        </div>
        <div class="cap"><b>Fig {idx+1}.</b> {fig1_cap}</div>
      </div>
"""
        elif idx == 1 and fig2_img:
            sections_body_html += f"""
      <div class="figure">
        <div class="frame">
          <img src="../uploads/projects/{fig2_img}" alt="{fig2_cap}" loading="lazy" />
        </div>
        <div class="cap"><b>Fig {idx+1}.</b> {fig2_cap}</div>
      </div>
"""

    gallery_html = "".join([f"""
        <div class="frame">
          <img src="../uploads/projects/{img_file}" alt="{img_caption}" loading="lazy" />
          <div class="g-caption">{img_caption}</div>
        </div>""" for img_file, img_caption in gallery_imgs])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} — Project Detail · Nabil Karim</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<style>
  :root{{
    --bg:#090909;
    --surface:#111111;
    --fg:#EDEDED;
    --muted:#666666;
    --divider:#1C1C1C;
    --accent:#F05E1C;
    --accent-glow:rgba(240,94,28,0.35);
    --mono:"IBM Plex Mono", ui-monospace, monospace;
    --sans:"DM Sans", system-ui, sans-serif;
    --gutter:clamp(20px, 5vw, 80px);
    --maxw:1280px;
  }}
  *{{box-sizing:border-box;margin:0;padding:0;}}
  html{{scroll-behavior:smooth;}}
  body{{
    background:var(--bg); color:var(--fg);
    font-family:var(--sans); line-height:1.6;
    -webkit-font-smoothing:antialiased;
    background-image:
      linear-gradient(rgba(237,237,237,0.018) 1px, transparent 1px),
      linear-gradient(90deg, rgba(237,237,237,0.018) 1px, transparent 1px);
    background-size: 48px 48px;
    background-attachment: fixed;
    cursor:none;
  }}
  body::before{{
    content:""; position:fixed; inset:0;
    pointer-events:none; z-index:9998;
    background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.55 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='0.18'/></svg>");
    mix-blend-mode:overlay; opacity:0.5;
  }}
  ::selection{{background:var(--accent); color:#000;}}

  .cursor{{
    position:fixed; top:0; left:0;
    width:18px; height:18px;
    pointer-events:none; z-index:9999;
    transform:translate(-50%,-50%);
    transition:opacity .15s ease, transform .08s linear;
  }}
  .cursor::before, .cursor::after{{
    content:""; position:absolute; background:var(--accent);
    box-shadow:0 0 8px var(--accent-glow);
  }}
  .cursor::before{{ left:50%; top:0; bottom:0; width:1px; transform:translateX(-50%); }}
  .cursor::after{{ top:50%; left:0; right:0; height:1px; transform:translateY(-50%); }}
  .cursor .dot{{
    position:absolute; left:50%; top:50%;
    width:4px; height:4px; background:var(--accent);
    border-radius:50%; transform:translate(-50%,-50%);
    box-shadow:0 0 6px var(--accent-glow);
  }}
  .cursor.hover{{ transform:translate(-50%,-50%) scale(1.6); }}
  @media (hover:none){{ body{{ cursor:auto; }} .cursor{{ display:none; }} }}

  nav.top{{
    position:fixed; top:0; left:0; right:0; z-index:100;
    padding:18px 0;
    background:rgba(9,9,9,0.72);
    backdrop-filter:blur(14px) saturate(140%);
    border-bottom:1px solid var(--divider);
  }}
  nav.top .wrap{{
    max-width:var(--maxw); margin:0 auto; padding:0 var(--gutter);
    display:flex; align-items:center; justify-content:space-between;
  }}
  .brand{{
    font-family:var(--mono); font-weight:700; font-size:18px;
    color:var(--fg); text-decoration:none; letter-spacing:-0.01em; cursor:none;
  }}
  .brand .dot{{ color:var(--accent); }}
  .back{{
    font-family:var(--mono); font-size:12px; letter-spacing:0.14em; text-transform:uppercase;
    color:var(--muted); text-decoration:none; display:inline-flex; align-items:center; gap:8px;
    transition:color .2s ease; cursor:none;
  }}
  .back:hover{{ color:var(--accent); }}

  .case-hero{{
    padding:140px 0 40px; border-bottom:1px solid var(--divider);
    position:relative;
  }}
  .wrap{{ max-width:var(--maxw); margin:0 auto; padding:0 var(--gutter); }}

  .breadcrumbs{{
    display:flex; align-items:center; gap:10px;
    font-family:var(--mono); font-size:11px; letter-spacing:0.18em; text-transform:uppercase;
    color:var(--muted); margin-bottom:24px;
  }}
  .breadcrumbs a{{ color:var(--muted); text-decoration:none; transition:color .2s ease; cursor:none; }}
  .breadcrumbs a:hover{{ color:var(--accent); }}
  .breadcrumbs .sep{{ opacity:0.4; }}
  .breadcrumbs .cur{{ color:var(--accent); }}

  .meta-tag{{
    display:inline-flex; align-items:center; gap:8px;
    font-family:var(--mono); font-size:10px; letter-spacing:0.2em; text-transform:uppercase;
    color:var(--accent); border:1px solid var(--accent); padding:4px 10px; margin-bottom:18px;
  }}

  h1.case-title{{
    font-family:var(--mono); font-weight:600; font-size:clamp(28px, 4.4vw, 48px);
    line-height:1.15; letter-spacing:-0.02em; color:var(--fg); margin-bottom:16px;
  }}
  p.case-sub{{
    font-size:clamp(16px, 1.8vw, 19px); color:var(--fg); opacity:0.75;
    max-width:820px; line-height:1.6; margin-bottom:36px;
  }}

  .case-meta-grid{{
    display:grid; grid-template-columns:repeat(4, 1fr); gap:18px;
    padding:24px 0; border-top:1px solid var(--divider); border-bottom:1px solid var(--divider);
  }}
  .meta-cell .label{{
    font-family:var(--mono); font-size:10px; letter-spacing:0.2em; text-transform:uppercase;
    color:var(--muted); margin-bottom:6px;
  }}
  .meta-cell .val{{ font-family:var(--mono); font-size:13px; color:var(--fg); }}
  @media (max-width:820px){{ .case-meta-grid{{ grid-template-columns:1fr 1fr; }} }}

  /* Hero Cover Media */
  .hero-media{{
    margin:36px 0 10px;
    width:100%; height:clamp(280px, 45vh, 520px);
    border:1px solid var(--divider);
    background:#0d0d0d;
    overflow:hidden; position:relative;
    display:flex; align-items:center; justify-content:center;
  }}
  .hero-media img{{
    width:100%; height:100%; object-fit:contain;
    background:#080808;
  }}

  .content{{
    padding:60px 0 100px;
    display:grid; grid-template-columns:280px 1fr; gap:64px;
    position:relative;
  }}

  aside.toc{{
    position:sticky; top:100px; height:fit-content;
    border-left:1px solid var(--divider); padding-left:20px;
  }}
  .toc-title{{
    font-family:var(--mono); font-size:11px; letter-spacing:0.2em; text-transform:uppercase;
    color:var(--muted); margin-bottom:16px;
  }}
  .toc ul{{ list-style:none; }}
  .toc li{{ margin-bottom:12px; }}
  .toc a{{
    font-family:var(--mono); font-size:12px; color:var(--fg); opacity:0.6;
    text-decoration:none; display:flex; align-items:baseline; gap:8px;
    transition:opacity .2s ease, color .2s ease; cursor:none;
  }}
  .toc a:hover{{ opacity:1; color:var(--accent); }}
  .toc a .num{{ color:var(--accent); opacity:0.5; font-size:10px; }}

  .body{{ min-width:0; }}
  .body section{{ margin-bottom:48px; }}
  .body h2{{
    font-family:var(--mono); font-weight:600; font-size:22px; letter-spacing:-0.01em;
    color:var(--fg); margin:36px 0 16px; display:flex; align-items:baseline; gap:12px;
  }}
  .body h2 .num{{ color:var(--accent); opacity:0.6; font-size:13px; letter-spacing:0.18em; }}
  .body h3{{ font-family:var(--mono); font-weight:500; font-size:15px; color:var(--accent); margin:24px 0 8px; }}
  .body p{{ font-size:15.5px; color:var(--fg); margin-bottom:18px; line-height:1.75; opacity:0.88; }}
  .body p strong{{ color:var(--accent); font-family:var(--mono); font-size:0.96em; font-weight:600; }}
  .body ul{{ list-style:none; margin:0 0 20px 0; }}
  .body ul li{{
    font-size:15px; padding-left:24px; position:relative; margin-bottom:10px; line-height:1.7;
    color:var(--fg); opacity:0.86;
  }}
  .body ul li::before{{ content:"—"; position:absolute; left:0; top:0; color:var(--accent); font-family:var(--mono); }}

  .metrics{{ display:grid; grid-template-columns:repeat(4, 1fr); gap:12px; margin:32px 0 24px; }}
  .metric{{ padding:18px 16px; border:1px solid var(--divider); background:var(--surface); position:relative; }}
  .metric::before{{ content:""; position:absolute; top:0; left:0; right:0; height:2px; background:var(--accent); opacity:0.8; }}
  .metric .n{{
    font-family:var(--mono); font-weight:600; font-size:24px; color:var(--accent);
    line-height:1.1; margin-bottom:6px; letter-spacing:-0.02em;
  }}
  .metric .lbl{{ font-family:var(--mono); font-size:9.5px; letter-spacing:0.18em; text-transform:uppercase; color:var(--muted); }}
  @media (max-width:760px){{ .metrics{{ grid-template-columns:1fr 1fr; }} }}

  .figure{{ margin:32px 0; }}
  .figure .frame{{
    width:100%; aspect-ratio:16/10; border:1px solid var(--divider);
    background:#0c0c0c; overflow:hidden; display:flex; align-items:center; justify-content:center;
  }}
  .figure .frame img{{
    width:100%; height:100%; object-fit:contain; background:#080808;
  }}
  .figure .cap{{ margin-top:10px; font-family:var(--mono); font-size:11px; letter-spacing:0.04em; color:var(--muted); }}
  .figure .cap b{{ color:var(--accent); font-weight:500; margin-right:6px; }}

  .gallery{{ display:grid; grid-template-columns:repeat(3, 1fr); gap:14px; margin:32px 0; }}
  .gallery .frame{{
    aspect-ratio:1/1; position:relative; overflow:hidden; border:1px solid var(--divider); background:#0c0c0c;
    display:flex; flex-direction:column;
  }}
  .gallery .frame img{{
    width:100%; height:100%; object-fit:cover; transition:transform .3s ease;
  }}
  .gallery .frame:hover img{{ transform:scale(1.05); }}
  .gallery .g-caption{{
    position:absolute; bottom:0; left:0; right:0; padding:6px 10px;
    background:rgba(9,9,9,0.85); font-family:var(--mono); font-size:10px; color:var(--fg);
    border-top:1px solid var(--divider);
  }}
  @media (max-width:760px){{ .gallery{{ grid-template-columns:1fr; }} }}

  .stack-chips{{ display:flex; flex-wrap:wrap; gap:6px; margin:12px 0 28px; }}
  .stack-chips .t{{
    font-family:var(--mono); font-size:10.5px; color:var(--muted); padding:4px 9px; border:1px solid var(--divider);
    transition:border-color .2s ease, color .2s ease;
  }}
  .stack-chips .t:hover{{ border-color:var(--accent); color:var(--accent); }}

  code{{ background:#161616; padding:2px 6px; color:var(--accent); font-family:var(--mono); font-size:12.5px; border-radius:2px; }}

  .case-foot{{ margin-top:60px; padding-top:32px; border-top:1px solid var(--divider); display:flex; flex-direction:column; gap:20px; }}
  .case-foot .author{{ display:flex; align-items:center; gap:12px; font-family:var(--mono); font-size:12px; letter-spacing:0.06em; color:var(--muted); }}
  .case-foot .pip{{ width:6px; height:6px; background:var(--accent); border-radius:50%; box-shadow:0 0 6px var(--accent-glow); }}

  .foot-nav{{
    display:flex; justify-content:space-between; align-items:center; gap:16px;
    margin-top:10px; padding-top:20px; border-top:1px solid var(--divider);
    font-family:var(--mono); font-size:12px; letter-spacing:0.12em; text-transform:uppercase;
  }}
  .foot-nav a{{ color:var(--fg); text-decoration:none; transition:color .2s ease; cursor:none; display:flex; align-items:center; gap:8px; }}
  .foot-nav a:hover{{ color:var(--accent); }}

  @media (max-width:900px){{
    .content{{ grid-template-columns:1fr; gap:36px; }}
    aside.toc{{ position:static; }}
  }}
</style>
</head>
<body>

<div class="cursor" id="cursor"><span class="dot"></span></div>

<nav class="top">
  <div class="wrap">
    <a href="../index.html" class="brand">Nabil Karim<span class="dot">.</span></a>
    <a href="../index.html#projects" class="back">← Back to Portfolio</a>
  </div>
</nav>

<section class="case-hero">
  <div class="wrap">
    <div class="breadcrumbs">
      <a href="../index.html">Portfolio</a>
      <span class="sep">/</span>
      <a href="../index.html#projects">Projects</a>
      <span class="sep">/</span>
      <span class="cur">Case {num}</span>
    </div>

    <div class="meta-tag">{badge}</div>
    <h1 class="case-title">{title}</h1>
    <p class="case-sub">{subtitle}</p>

    <div class="case-meta-grid">
      <div class="meta-cell">
        <div class="label">Role</div>
        <div class="val">{role}</div>
      </div>
      <div class="meta-cell">
        <div class="label">Organization / Context</div>
        <div class="val">{client}</div>
      </div>
      <div class="meta-cell">
        <div class="label">Timeline</div>
        <div class="val">{period}</div>
      </div>
      <div class="meta-cell">
        <div class="label">Primary Focus</div>
        <div class="val">{stack[0]} &middot; {stack[1] if len(stack) > 1 else ""}</div>
      </div>
    </div>

    <!-- Hero Media Preview -->
    <div class="hero-media">
      <img src="../uploads/projects/{cover_img}" alt="{title} preview" loading="eager" />
    </div>
  </div>
</section>

<div class="wrap">
  <div class="content">
    <aside class="toc">
      <div class="toc-title">Table of Contents</div>
      <ul>
        {toc_html}
        <li><a href="#gallery"><span class="num">05</span><span>Visual Gallery</span></a></li>
        <li><a href="#tech-specs"><span class="num">06</span><span>Tech Specifications</span></a></li>
      </ul>
    </aside>

    <main class="body">
      <!-- Quick Metrics Strip -->
      <div class="metrics">
        {metrics_html}
      </div>

      <p style="font-size:16px; line-height:1.75; margin-bottom:28px;">
        <strong>Executive Summary:</strong> {summary}
      </p>

      <!-- Main Article Sections -->
      {sections_body_html}

      <!-- Visual Gallery Section -->
      <section id="gallery">
        <h2><span class="num">05</span>Visual Gallery & Technical Artifacts</h2>
        <p>Comprehensive photographs, schematics, 3D CAD models, and instrumentation traces extracted directly from the engineering project portfolio:</p>
        <div class="gallery">
          {gallery_html}
        </div>
      </section>

      <!-- Technology Stack -->
      <section id="tech-specs">
        <h2><span class="num">06</span>Core Engineering Toolchain</h2>
        <div class="stack-chips">
          {chips_html}
        </div>
      </section>

      <div class="case-foot">
        <div class="author">
          <span class="pip"></span>
          <span>Nabil Karim Abdurrahman &mdash; Engineering Physics, Institut Teknologi Bandung</span>
        </div>
        <div class="foot-nav">
          <a href="{prev_link}">← Prev: {prev_title[:28]}...</a>
          <a href="{next_link}">Next: {next_title[:28]}... →</a>
        </div>
      </div>
    </main>
  </div>
</div>

<script>
  // Custom cursor
  (function(){{
    const cursor = document.getElementById('cursor');
    if(!cursor) return;
    let cx = window.innerWidth/2, cy = window.innerHeight/2;
    window.addEventListener('mousemove', e=>{{
      cx = e.clientX; cy = e.clientY;
      cursor.style.left = cx + 'px';
      cursor.style.top = cy + 'px';
    }});
    const hoverables = document.querySelectorAll('a, button, .frame, .metric');
    hoverables.forEach(el=>{{
      el.addEventListener('mouseenter', ()=>cursor.classList.add('hover'));
      el.addEventListener('mouseleave', ()=>cursor.classList.remove('hover'));
    }});
  }})();
</script>
</body>
</html>"""

# Generate all 18 project files in both directories
target_dirs = [
    r"d:\project\porto26\projects",
    r"d:\project\porto26\project\projects"
]

for d in target_dirs:
    os.makedirs(d, exist_ok=True)

for i, proj in enumerate(PROJECTS):
    prev_proj = PROJECTS[i - 1]
    next_proj = PROJECTS[(i + 1) % len(PROJECTS)]
    html_content = generate_project_detail_html(proj, prev_proj, next_proj)
    
    for d in target_dirs:
        out_path = os.path.join(d, f"{proj['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_content)
    print(f"Generated: {proj['slug']}.html")

print("All 18 project detail pages generated successfully!")

