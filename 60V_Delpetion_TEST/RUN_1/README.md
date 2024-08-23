## Set-Up

Data taken with the standard MALTA2 parameters: 36.4um pixel pitch, 512 x 224 pixel matrix, 100um sensor thickness, 2ns integration time. Depletion voltage changed to -60V.

| Parameter        | Value                 |
|------------------|-----------------------|
| Sensor Dimension | 20.2 mm x 10.1168 mm  |
| Pixel Pitch      | 36.4 um x 36.4 um     |
| Pixel Matrix     | 512 x 224             |
| Sensor Thickness | 100 um                |
| Sensor Excess    | 0.7816 mm x 0.9812 mm |

: Table of sensor parameters

| Parameter              | Value   |
|------------------------|---------|
| Particle               | proton  |
| Energy                 | 180GeV  |
| Temperature            | 258.15K |
| Depletion Voltage      | -60V    |
| Digitisation Threshold | 260e    |

: Simulation operational parameters

Bias voltages = [0V, -6V, -9V, -15V, -20V, -25V, -30V, -50V]

## Results

![Cluster size vs. incident test beam angle](Plots/Cluster_Size.png)

![Cluster size vs. tan(angle)](Plots/tan(theta)_Cluster_Size.png)

![Linearly fitted cluster size data to produce depletion depth vs. bias voltage](Plots/Depletion_depth_linear_fit_comparison.png)
