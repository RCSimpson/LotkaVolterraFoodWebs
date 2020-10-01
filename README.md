# Lotka Volterra Food Webs

<p float="left">
<img src="https://upload.wikimedia.org/wikipedia/commons/1/16/Fox_-_British_Wildlife_Centre_(17429406401).jpg" width="50%" height="50%">

<img src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Domestic_white_rabbit_sitting_in_a_meadow.jpg" width="50%" height="50%">
</p>          

We can model complex predator-prey dynamics through systems of differential equations. These systems sometimes exhibit chaotic behavior provided that we have three or more species interacting. By simply increasing the dimensionality from two to three we introduce the possibility of chaos.

The programs and notebooks produce plots and animations of these dynamical systems. 

The animation below shows how one phase-plot of the Lotka-Volterra model might look:
### Two Species Lotka Volterra 
 <img src="https://github.com/RCSimpson/LotkaVolterraFoodWebs/blob/master/Images/Lotka_Volterra_Time.png" alt="Two-Species Model"> 

 <img src="https://github.com/RCSimpson/LotkaVolterraFoodWebs/blob/master/Images/lotkaVolterra2.gif" alt="Two-Species Model"> 

We see that the predator and prey population move in cylcical patterns given the parameter choices. If there is a large population of predators, more prey will be eaten, their population falling. The absence of food then causes the predator population to fall, thus allowing the prey animal to repopulate. 

### Three-plus Species Lotka Volterra 

However we know that animals live in eco-systems where animals may be either predators or prey. There may even be more complication animal relationships like symbiosis or scavenger-behavior. The Hastings model is a three dimensional Lotka-volterra model where rates of feeding are porportional to ratios of populations. Upon choosing certain parameter values the trajectories can generate strange attractors and thus exhibit chaos. We see below the classic tea-cup shape of the strange attractor that appears for this model. 

 <img src="https://github.com/RCSimpson/LotkaVolterraFoodWebs/blob/master/Images/Hastings_time.png" alt="Hastings Model"> 

 <img src="https://github.com/RCSimpson/LotkaVolterraFoodWebs/blob/master/Images/Hastings_phase.png" alt="Hastings Model"> 
 
 <img src="https://github.com/RCSimpson/LotkaVolterraFoodWebs/blob/master/Images/lotkaVolterra3.gif" alt="Hastings Model"> 

