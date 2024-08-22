## Introduction:

Hello everyone, I am Elliott, one of the UoB 2024 summer interns.My project has been validating the grazing angle method, which is used to determine the depletion depth of a sensor. For this investigation, a non-irradiated MALTA2 sensor was used. The motivation behind this was that Long had taken data with a sensor irradiated with 1 x 10$^{15}$ 1 MeV n$_{eq}$/cm$^2$ non ionising energy loss. We therefore wished to test whether an initial, more simplistic simulation would yield similar results to Long’s, thus verifying the use of the grazing angle method. Our sensor therefore had a linear electric field, as this was the simplest model other than a constant electric field. 


Now we know the basis of the investigation, let’s get into the finer details. To start, let’s look at why MALTA2 was created in the first place.

## HL - LHC Upgrade:

Beyond a certain lifetime, the LHC experiments, including ATLAS and LHCb, will begin to yield diminishing returns in terms of interesting physics. This is due to the radiation damage on the detector modules, and to interesting decays being too rare to be seen given the noise in the system. The solution to this problem is the high luminosity upgrade. The LHC will begin its third long shutdown in December this year, and will not be switched on again until July 2027, once the high luminosity upgrade is completed. One of our hopes is that we can take a measurement of the Higgs self-coupling. We can also search for physics beyond the standard model. But how do we achieve this, and what do we mean by a high luminosity upgrade. Well, the LHC instantaneous luminosity will be increased by a factor of 5 from its nominal value to 7.5 x 10$^{34}$ cm$^{-2}$ s$^{-1}$. This will increase the number of interactions per bunch crossing from 50 to 200. On the ATLAS detector side the pseudo-rapidity coverage will increase from 2.5 to 4, and the inner detector will be replaced by higher granularity, radiation hard sensors. The inner-most pixels will be 25 x 100 $\mu$m$^{2}$, while the rest of the pixel detector will still be based on the original 50 x 50 $\mu$m$^{2}$ pixel pitch.

## Hybrid Detectors:

These pixels are hybrids, which means the readout chip or ASIC is bump-bonded to the silicon sensor. The ASIC is segmented into pixels. This means we are limited in terms of pixel pitch, as well as requiring expensive glue for the bonding process. Our depletion depth is also only of the order of 1 micron. However, these shortcomings can be resolved with a Depleted Monolithic Active Pixel Sensor (DMAPS).

## DMAPS Benefits Over Hybrid Detectors:

DMAPS are advantageous over current hybrid sensors as they: can have a smaller pixel pitch, i.e. 36.4 x 36.4$\mu$m$^{2}$ squared for the MALTA2 sensor compared to 50 by 50 for the ATLAS ITk; contain one chip, not two; require a lower material budget without the glue. Seen in this figure is a standard CMOS DMAPS, with the readout electronics located at the top. One can also see that the depletion zone does not cover the full extent of the epitaxial layer. MALTA2 was targeted for the outermost layer in ATLAS ITk, however due to limited production, this was not achieved. One potential future use of MALTA2 is in the innermost ITk layer, although this will require improvements in its radiation hardness, which is currently target at 3 x 10\^15 1 MeV neutron equivalents per square centimetre.

Standard CMOS Sensors vs MALTA2:

MALTA2 is a modified DMAPS which contains a low dose n-type implant and an extra deep p-well. The implant here changes the depletion region such that it is more rectangular and covers the implant and epitaxial layers. The p-well here guides the electric field such that charge does not cross between the pixels. Thus, charge collection by drift, rather than diffusion, dominates, reducing charge sharing between pixels and increasing the signal to noise ratio.

Here you can see the depletion region boundaries of a DMAPS, with the depletion depth being of the order of 100 microns. This is an improvement on the 1 micron depletion depth for hybrid sensors.

The Grazing Angle Method:

Now that we have introduced the MALTA2 sensor, we want to characterise its radiation hardness. As previously mentioned, the aim for MALTA2 is 3 x 10\^15 1 MeV neutron equivalent per centimetre square. Current test beam data taken by Long, which will be presented in the coming weeks, was taken at 1/3 that value. One method of characterising radiation hardness is via the depletion depth. If the depletion depth has decreased compared to what is expected given the bias voltage, we may well conclude that the minority charge carrier lifetime has decreased. Thus, a lower proportion of electron-hole pairs produce observable signals in the detector. The grazing angle method is one method of determining the depletion depth, illustrated in this figure, showing how the cluster size for a given beam incident angle relates to the pixel pitch and depletion depth.

We can measure the cluster size, and we have the pixel pitch, so a simple rearrangement yields the depletion depth. However, we need to verify this method by simulating a similar sensor test beam investigation to Long’s.

Allpix Squared:

The simulation software chosen for this investigation was allpix squared. For those of you unfamiliar with allpix squared, it is a Monte Carlo simulation software that uses Geant4 to simulate charge-matter interactions. And if you don’t know Geant4, it is a software used for modelling the propagation of charges through materials. If you’re anything like me, visualising your set-up is a good example of a quick sanity check that your simulation is running. The figure here shows the simulation set-up for the telescope test beam simulation, where the blue line is the proton beam. We use 7 MALTA2 sensors, with the fourth being the device under test (DUT), the sensor being rotated. Another aspect of allpix that is helpful is the readability of the configuration files, and the well documented modules that can be found here.

The MALTA2 Sensor:

Included here are the parameters for the MALTA2 sensor.

Simulation Set-Up:

Then the following test beam, environmental and digitisation parameters were used. All, except the depletion voltage were identical to Long’s irradiated sensor investigation. For the voltage, the largest value used by Long was taken to be the full depletion voltage as an initial guess. The depletion voltage represents the voltage at which the whole sensor is fully depleted, i.e. free of charge carriers (electrons and holes that is).

Simulation Workflow:

At the centre of our investigation is the simulation workflow. Don’t worry if you can’t read the points well enough here, we will move through them sequentially to show how the simulation works.

Firstly, we have the table of applied bias voltages, each of which are implemented sequentially into a linear electric field of the following form and give the depletion width of our sensor.

The field and its width give the following electric field form, with a linear region, and a fully undepleted region.

This electric field allows charges to propagate in the z-axis towards the collection electrode at the top of the sensor. Because our clustering data should be angle dependent, we cycle through angles between 0 – 60 degrees in 5-degree increments. This is done for each of the bias voltages. This combined with the electric field creates a test beam experiment cycling through angles and bias voltages and yields the average cluster size for each of these parameters.

Simulation Implementation:

All this visualisation is all well and good, but how do we program this in allpix squared. Well, with the configuration files I previously mentioned, we can implement each of the modules using headers such as Deposition Geant4 and Electric Field Reader.

Cluster Size Data:

The data for the full telescope investigation can be seen here. The first thing to observe is that the cluster size at zero degrees decreases with increasing bias voltage. This implies that the increasing electric field limits the amount of charge sharing between the pixels. Alongside this data is Long’s irradiated sensor data, which is placed here for a simple comparison. We can see that Long’s data and the allpix generated data do not match, as low biases here yield higher cluster sizes, but Long’s data yield lower cluster sizes.

Depletion Depth vs Incident Angle:

By taking the grazing angle equation from before and after rearranging, we can calculate the depletion depth for each bias voltage at each measured angle. Once again, Long’s data is there for comparison. At lower bias voltage, the simulated depletion depth is lower than for higher bias, and this relationship is also seen in Long’s data. This is to be expected as a higher electric field should increase the depletion width. A major discrepancy between the two is that for the simulation, increasing the angle increases the depletion depth, whereas experimentally, the variation is small and not always increasing with increasing angle. This shows that the simple application of the rearranged grazing angle equation is not valid as the depletion depth should not be dependent on the incident angle.

Linear fit to depletion depth:

Scaling the x-axis of the cluster size data by taking tan of each angle, we obtain the figure here. The cluster size equation is reproduced here. The graph should follow a linear relationship in tan angle, with the depletion depth divided by the pixel pitch being the gradient. Given the failure of the previous depletion depth calculation, we applied a linear fit to the data. As linearity appeared to only be present beyond tan(angle) \> 0.5, we ignored the points before this in our fit.

These fits yield the graph here, where the fitted points are placed along with the calculated points based on the depletion width. It can clearly be seen that the data is not in agreement with expectation. We therefore had to determine the nature of this higher-than-expected depletion depth.

Linear Electric Field Investigation:

Our first course of action was to look at the electric field. We know already that when the bias voltage is below the depletion voltage, the electric field gets cut-off at a certain thickness. The initial guess was that the diffusion charges propagating in these undepleted regions still contribute to the signal, and therefore to the clustering data. To test this, we had to essentially cut-off the sensor at the boundary between the depleted and undepleted regions, while maintaining the same electric field in the depletion region. This was achieved by calculating the width of the depletion region at each bias voltage, assuming that at –30 volts the depth is 100 microns. We could then reduce the thickness of the sensor to that value, and fully bias it with a depletion voltage equal to the old bias voltage.

Linear Electric Field Investigation Method

Here is an example for –15 volts bias. Applying this method to every bias voltage, we obtained this cluster size against tan angle graph.

Linear Electric Field Investigation Results

We see now that lower bias voltages yield reduced cluster sizes compared to higher biases. Despite this change, linearity is still only observed above tan(angle) \> 0.5. To investigate what this means for the depletion depth, a linear fit was once again applied.

These linear fits show good conformity to the calculated depletion width values, indicating that our initial hypothesis of diffusion charges affecting the clustering data is valid.

We can see here the two collections of fits side by side. This provided the evidence to pursue a further investigation of the diffusion charges.

Lineplots and Hitmap Method:

We have previously shown a lineplots graph in this presentation, however their use only becomes apparent when compared to the equivalent hitmap. It was therefore decided that lineplots and hitmaps would be taken to visually see what goes on for different bias voltages. Included here are a sample of them using 1-micron pixel pitch for increased granularity and a 10nm beam size for more precise, repeatable hits on the sensor. An important note here is that all the telescope sensors, apart from the DUT, were removed for this investigation and onwards.

At 0 volts, no electric field is present so the only contribution to the recorded signal is via diffusion charges. A yet unexplained symmetry is present in the hitmap at 45 degrees.

Moving on to -15 volts, i.e. half the depletion voltage, we see diffusion charges are only significantly present in the undepleted region, as expected. On the hitmap, a bulbous shower is seen towards the test beam entrance. This likely represents the diffusion charges, as this shape is only significant in the undepleted region.

At full -30 volts depletion, the bulbous shower reduces in extent and thickness. To note on the lineplot is that the charged beam track is stopped here, also visible on the hitmap here. This cut-off, it was discovered, is mediated by the integration time, which is automatically set to 25 ns, the bunch crossing separation in the LHC. This is the time over which charge carrier propagation is counted.

Finally, an overbiased -50 volts measurement was taken, which further reduced the spread of charge carriers.

Integration Time:

It was then suspected that integration time may be affecting the result. After all, the diffusion charges do require a significant time to reach the collection electrode as their motion is mediated by thermodynamic processes. Therefore, measurements without the telescope were taken with integration times of 25ns, 2ns, and 10ps. The results of the cluster size vs tan(angle) are shown here. The results throw up more questions as the expected effect of reducing the clustering at 0 degrees by removing diffusion charge sharing was not realised. Instead, the data all converges to the original 25ns, –30V data. Once again, a linear fit was applied to this data, again for tan(angle) \> 0.5.

Depletion depth:

As previously seen, the data appears to be giving results closer to a fully depleted sensor, despite the reduction in the integration time. A further analysis of the effect of integration time must be undertaken.

60V Depletion Voltage

Data was taken at –60V as unirradiated data taken by Long indicated the depletion depth to be –60V. Here we see the cluster size against tan(angle) data, and once again fits for tan(angle) \> 0.5 were produced. The behaviour of the depletion depth against bias voltage is no different to when the depletion voltage was –30V. The sensor still has a higher than predicted depletion depth for each bias voltage.

Conclusion:

In conclusion, we have seen that the determination of the depletion depth of a sensor via the grazing angle method is not fully understood. At low angles and bias voltages it is suspected that diffusion charges play a significant role, reducing the depletion depth’s conformity to what is predicted. To understand this behaviour further, we must improve the sophistication of our simulation. The most obvious way to do this is by replacing the linear electric field with a mesh field constructed in a TCAD software such as sentaurus device editor. However, visualisation does not work currently, so this was unattainable in the timeframe of the internship. However, with such software we could add the n-gap, extra deep p-well, and CMOS technology to shape the electric field to be closer to that of MALTA2.

Thank you very much for listening and generally welcoming me into your group. It has been a pleasure to work with you all.
