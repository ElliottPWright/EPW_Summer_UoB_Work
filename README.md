# The Project

## Introduction:

Hello everyone, I am Elliott, one of the UoB 2024 summer interns. My project has been validating the grazing angle method, which is used to determine the depletion depth of a sensor. For this investigation, a simulation of a non-irradiated MALTA2 sensor constructed. The motivation behind this was that data had already been with a sensor irradiated with 1 x 10$^{15}$ 1 MeV n$_{eq}$/cm$^2$ non ionising energy loss. We therefore wished to test whether an initial, more simplistic simulation would yield similar results to experiment, thus verifying the use of the grazing angle method. Our sensor therefore had a linear electric field, as this was the simplest model other than a constant electric field. Included below is a brief outline of how this repository is organised, a summary of the main experiments conducted, and the conclusions so far.

## Layout of the GitHub Repository

This repository is organised into experiments, simulation files, and miscellaneous content such as Helpful_Documents. Each experiment contains a certain number of runs, which just represents the number of times I have conducted an experiment of a certain type. Within each run is CSV data for the cluster sizes on a sensor, and the ROOT files that contain the raw outputted data. If I felt the data was worth further investigation, there will also be plots included.

## The Experiments

Going chronologically, and negating some of the experiments that went no-where, the first experiment was Full_Telescope_RUN. In this investigation, a testbeam of 180 GeV proton was fired at 7 MALTA2 sensors, the fourth of which was our device under test (DUT). This DUT was rotated about the x-axis in 5-degree increments from 0 - 60 degrees. Increasing bias voltages, up to the depletion voltage of -30V, were applied to the sensor and the average cluster size was recorded for each angle at each bias voltage. 

After this, we began to suspect that diffusion charges were altering our clustering data to not match experimental behaviour. We therefore then started Electric_Field_Reader_TESTS, where we wanted to see what would happen if the undepleted (drift) region of the sensor was cut-off, so all we had was the depleted (drift) region. We had to cut-off the sensor at the boundary between the depleted and undepleted regions, while maintaining the same electric field in the depletion region. This was achieved by calculating the width of the depletion region at each bias voltage, assuming that at –30 volts the depth is 100 microns. We could then reduce the thickness of the sensor to that value, and fully bias it with a depletion voltage equal to the old bias voltage. This investigation yielded results that better conformed to experiment. 


Next, with evidence to suggest that our data was skewed by the diffusion charges, we began Lineplot_Hitmap_Data. We decided that lineplots and hitmaps would be taken to visually see what goes on for different bias voltages. Using 1-micron pixel pitch for increased granularity and a 10nm beam size for more precise, repeatable hits on the sensor, data was taken with 1 event for the lineplots and 10E4 events for the hitmaps. An important note here is that all the telescope sensors, apart from the DUT, were removed for this investigation and onwards.


Finally, in Collection_Timing_TESTS, an attempt was made to remove the diffusion charges by reducing the integration time, i.e. the time over which e/h pairs are propagated. As diffusion charges are moderated by thermodynamic processes, compared to drift charges which move to the collection electrode by the electric field, they move slower. Therefore, we reduced the integration time from 25ns to 2ns and then finally to 10ps, however this yielded an undesired effect. Instead, the data all converged to the original 25ns, –30V data.


## Conclusions:

In conclusion, we have seen that the determination of the depletion depth of a sensor via the grazing angle method is not fully understood. At low angles and bias voltages it is suspected that diffusion charges play a significant role, reducing the depletion depth’s conformity to what is predicted. To understand this behaviour further, we must improve the sophistication of our simulation. The most obvious way to do this is by replacing the linear electric field with a mesh field constructed in a TCAD software such as sentaurus device editor. However, visualisation does not work currently, so this was unattainable in the timeframe of the internship. However, with such software we could add the n-gap, extra deep p-well, and CMOS technology to shape the electric field to be closer to that of MALTA2.


# Appendicies

## Introduction

The following appendices are based on the presentation I gave to the University of Birmingham BILPA group. They should be read to give some context on the project. The reader is also directed to PRESENTATION_NOTES to see the presentation and associated speech, as well as Helpful_Documents for further reading. Now let's get to some context.

## HL - LHC Upgrade:

Beyond a certain lifetime, the LHC experiments, including ATLAS and LHCb, will begin to yield diminishing returns in terms of interesting physics. This is due to the radiation damage on the detector modules, and to interesting decays being too rare to be seen given the noise in the system. The solution to this problem is the high luminosity upgrade. The LHC will begin its third long shutdown in December this year, and will not be switched on again until July 2027, once the high luminosity upgrade is completed. One of our hopes is that we can take a measurement of the Higgs self-coupling. We can also search for physics beyond the standard model. But how do we achieve this, and what do we mean by a high luminosity upgrade. Well, the LHC instantaneous luminosity will be increased by a factor of 5 from its nominal value to 7.5 x 10$^{34}$ cm$^{-2}$ s$^{-1}$. This will increase the number of interactions per bunch crossing from 50 to 200. On the ATLAS detector side the pseudo-rapidity coverage will increase from 2.5 to 4, and the inner detector will be replaced by higher granularity, radiation hard sensors. The inner-most pixels will be 25 x 100 $\mu$m$^{2}$, while the rest of the pixel detector will still be based on the original 50 x 50 $\mu$m$^{2}$ pixel pitch.

## Hybrid Detectors:

These pixels are hybrids, which means the readout chip or ASIC is bump-bonded to the silicon sensor. The ASIC is segmented into pixels. This means we are limited in terms of pixel pitch, as well as requiring expensive glue for the bonding process. Our depletion depth is also only of the order of 1 micron. However, these shortcomings can be resolved with a Depleted Monolithic Active Pixel Sensor (DMAPS).

## DMAPS Benefits Over Hybrid Detectors:

DMAPS are advantageous over current hybrid sensors as they: can have a smaller pixel pitch, i.e. 36.4 x 36.4$\mu$m$^{2}$ squared for the MALTA2 sensor compared to 50 by 50 for the ATLAS ITk; contain one chip, not two; require a lower material budget without the glue. Seen in this figure is a standard CMOS DMAPS, with the readout electronics located at the top. One can also see that the depletion zone does not cover the full extent of the epitaxial layer. MALTA2 was targeted for the outermost layer in ATLAS ITk, however due to limited production, this was not achieved. One potential future use of MALTA2 is in the innermost ITk layer, although this will require improvements in its radiation hardness, which is currently target at 3 x 10\^15 1 MeV neutron equivalents per square centimetre.

## Standard CMOS Sensors vs MALTA2:

MALTA2 is a modified DMAPS which contains a low dose n-type implant and an extra deep p-well. The implant changes the depletion region such that it is more rectangular and covers the implant and epitaxial layers. The p-well guides the electric field such that charge does not cross between the pixels. Thus, charge collection by drift, rather than diffusion, dominates, reducing charge sharing between pixels and increasing the signal to noise ratio.

## The Grazing Angle Method:

Now that we have introduced the MALTA2 sensor, we want to characterise its radiation hardness. As previously mentioned, the aim for MALTA2 is 3 x 10\^15 1 MeV neutron equivalent per centimetre square. Current test beam data taken experimentally, was taken at 1/3 that value. One method of characterising radiation hardness is via the depletion depth. If the depletion depth has decreased compared to what is expected given the bias voltage, we may well conclude that the minority charge carrier lifetime has decreased. Thus, a lower proportion of electron-hole pairs produce observable signals in the detector. The grazing angle method is one method of determining the depletion depth, showing how the cluster size for a given beam incident angle relates to the pixel pitch and depletion depth. We can measure the cluster size, and we have the pixel pitch, so a simple rearrangement yields the depletion depth. However, we need to verify this method by simulating a similar sensor test beam investigation to the experiment.

## Allpix Squared:

The simulation software chosen for this investigation was allpix squared. For those of you unfamiliar with allpix squared, it is a Monte Carlo simulation software that uses Geant4 to simulate charge-matter interactions. And if you don’t know Geant4, it is a software used for modelling the propagation of charges through materials. If you’re anything like me, visualising your set-up is a good example of a quick sanity check that your simulation is running. We use 7 MALTA2 sensors, with the fourth being the device under test (DUT), the sensor being rotated. Another aspect of allpix that is helpful is the readability of the configuration files, and the well documented modules.
