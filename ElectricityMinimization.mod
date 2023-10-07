/*********************************************
 * OPL 22.1.1.0 Model
 * Author: thaki
 * Creation Date: Oct 6, 2023 at 3:12:21 PM
 *********************************************/
 
 using CP;
 
//Variables                                             Decision Variables
int numTimeSlots = ...;
range timeSlotIndices = 1..numTimeSlots;

int isThisTimeSlotInPeakHours[timeSlotIndices] = ...;


//Fridge related
int numFridges = ...;
range fridgeIndices = 1..numFridges;

int isFridgeOnInThisTimeSlot[timeSlotIndices] = ...;

float costOfFridgePerQuarterHour[1..2][1..2] = ...;

                                                        dvar boolean isThisFridgeOnInThisTimeSlot[fridgeIndices][timeSlotIndices];
                                                        
                                                        dexpr float costForFridges = 
                                                            sum(fridge in fridgeIndices,
                                                                timeSlot in timeSlotIndices) isThisFridgeOnInThisTimeSlot[fridge][timeSlot] * costOfFridgePerQuarterHour[isThisTimeSlotInPeakHours[timeSlot] + 1]
																																										[isThisFridgeOnInThisTimeSlot[fridge][timeSlot] + 1];
//Oven Related
float costOfOvenPerQuarterHour[1..2][1..2]   = ...;																						 
                                                        dvar boolean
                                                            isOvenOnInThisTimeSlot[timeSlotIndices];
														
                                                        dexpr float costForOven = 
                                                            sum(timeSlot in timeSlotIndices)
                                                                isOvenOnInThisTimeSlot[timeSlot] * costOfOvenPerQuarterHour[isThisTimeSlotInPeakHours[timeSlot] + 1]
                                                                                                                           [isOvenOnInThisTimeSlot[timeSlot] + 1];

minimize costForFridges +
         costForOven;


subject to
{
    //Fridge is On in peak hours only
    forall(fridge in fridgeIndices)
        forall(timeSlot in timeSlotIndices)
        {
            isThisFridgeOnInThisTimeSlot[fridge]
                                        [timeSlot] == isFridgeOnInThisTimeSlot[timeSlot];
        }

    //Oven is On only for 15 mins
    sum(timeSlot in timeSlotIndices) isOvenOnInThisTimeSlot[timeSlot] == 1; 
}