# Harms

## Lung damage { .harm #lung-damage }

Reversable lung damage causing discomfort to pain for a few days.

## Cut in skin { .harm #skin-cut }

Reversable skin cut causing discomfort for a day or two.

## Decapitation { .harm #decapitation }

Irreversible removal of head leading to immediate death.

# Hazard

## Tripwire { .hazard #trip-wire }

Metal wire that can trip people up. Could be variable height.

## Paper edge { .hazard #paper-edge }

A cut edge of a piece of paper.

## Chlorine gas { .hazard #chlorine-gas }

Chlorine gas is stored in a little vial.

# Hazardous Situation

## Tripwire deployed at neck height { .hazardous-situation #trip-wire-deployed-neck-high }

The [#trip-wire] being deployed at neck height could lead to [decapitation](#decapitation).

## Printer outputs paper next to user's fingers { .hazardous-situation #paper-cut }

Outputting paper gives a [#paper-edge], which, while the user
has a finger nearby could produce a [skin cut](#skin-cut).

## Vial is broken { .hazardous-situation #broken-vial }

If the vial is broken the [#chlorine-gas] will be released
leading to possible [lung damage](#lung-damage).

# Specific Software Causes

## Tripwire deployment while deployer in heck-high position { .software-cause #neck-high-tripwire-deployment }

The [module:tripwire#deploy] could deploy erroneously leading to the [trip wire being deployed at neck height](#trip-wire-deployed-neck-high)

## Actuator activated while arm is next to chlorine vial { .software-cause #actuator-breaks-vial }

[module:actuator#activate] could fire erroneously leadint to [Chlorine gas](#chlorine-gas)

# Risk Mitigation

## Output printer while 1, 4 or 7 buttons are pressed { .risk-mitigation #paper-feed-suppressed-147 }

If paper is output while the user is pressing the buttons 1, 4 or 7 a [paper cut](#paper-cut) may be produced, so we will suppress paper feeds while the 1, 4 or 7 buttons are being activated.
