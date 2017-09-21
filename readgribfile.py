# -*- coding:utf-8 -*- 
import struct
import numpy as np

identificationOfOriginatingOrGeneratingCenterDic= { \
						'00': 'WMO Secretariat' ,\
						'01': 'Melbourne' ,\
						'02': 'Melbourne' ,\
						'03': 'Melbourne' ,\
						'04': 'Moscow' ,\
						'05': 'Moscow' ,\
						'06': 'Moscow' ,\
						'07': 'US National Weather Service, National Centers for Environmental Prediction (NCEP)' ,\
						'08': 'US National Weather Service Telecommunications Gateway (NWSTG)' ,\
						'09': 'US National Weather Service - Other' ,\
						'10': 'Cairo (RSMC/RAFC)' ,\
						'11': 'Cairo (RSMC/RAFC)' ,\
						'12': 'Dakar (RSMC/RAFC)' ,\
						'13': 'Dakar (RSMC/RAFC)' ,\
						'14': 'Nairobi (RSMC/RAFC)' ,\
						'15': 'Nairobi (RSMC/RAFC)' ,\
						'18': 'Tunis-Casablanca (RSMC)' ,\
						'19': 'Tunis-Casablanca (RSMC)' ,\
						'20': 'Las Palmas (RAFC)' ,\
						'21': 'Algiers (RSMC)' ,\
						'24': 'Pretoria (RSMC)' ,\
						'25': 'La Réunion (RSMC)' ,\
						'26': 'Khabarovsk (RSMC)' ,\
						'27': 'Khabarovsk (RSMC)' ,\
						'28': 'New Delhi (RSMC/RAFC)' ,\
						'29': 'New Delhi (RSMC/RAFC)' ,\
						'30': 'Novosibirsk (RSMC)' ,\
						'31': 'Novosibirsk (RSMC)' ,\
						'32': 'Tashkent (RSMC)' ,\
						'33': 'Jeddah (RSMC)' ,\
						'34': 'Tokyo (RSMC), Japan Meterological Agency' ,\
						'35': 'Tokyo (RSMC), Japan Meterological Agency' ,\
						'36': 'Bangkok' ,\
						'37': 'Ulan Bator' ,\
						'38': 'Beijing (RSMC)' ,\
						'39': 'Beijing (RSMC)' ,\
						'40': 'Seoul' ,\
						'41': 'Buenos Aires (RSMC/RAFC)' ,\
						'42': 'Buenos Aires (RSMC/RAFC)' ,\
						'43': 'Brasilia (RSMC/RAFC)' ,\
						'44': 'Brasilia (RSMC/RAFC)' ,\
						'45': 'Santiago' ,\
						'46': 'Brazilian Space Agency - INPE' ,\
						'51': 'Miami (RSMC/RAFC)' ,\
						'52': 'Miami (RSMC/RAFC), National Hurricane Center' ,\
						'53': 'Montreal (RSMC)' ,\
						'54': 'Montreal (RSMC)' ,\
						'55': 'San Francisco' ,\
						'57': 'US Air Force - Air Force Global Weather Central' ,\
						'58': 'Fleet Numerical Meteorology and Oceanography Center, Monterey, CA, USA' ,\
						'59': 'The NOAA Forecast Systems Laboratory, Boulder, CO, USA' ,\
						'60': 'United States National Center for Atmospheric Research (NCAR)' ,\
						'64': 'Honolulu' ,\
						'65': 'Darwin (RSMC)' ,\
						'66': 'Darwin (RSMC)' ,\
						'67': 'Melbourne (RSMC)' ,\
						'69': 'Wellington (RSMC/RAFC)' ,\
						'70': 'Wellington (RSMC/RAFC)' ,\
						'71': 'Nadi (RSMC)' ,\
						'74': 'UK Meteorological Office, Bracknell (RSMC)' ,\
						'75': 'UK Meteorological Office, Bracknell (RSMC)' ,\
						'76': 'Moscow (RSMC/RAFC)' ,\
						'78': 'Offenbach (RSMC)' ,\
						'79': 'Offenbach (RSMC)' ,\
						'80': 'Rome (RSMC)' ,\
						'81': 'Rome (RSMC)' ,\
						'82': 'Norrköping' ,\
						'83': 'Norrköping' ,\
						'85': 'Toulouse (RSMC)' ,\
						'86': 'Helsinki' ,\
						'87': 'Belgrade' ,\
						'88': 'Oslo' ,\
						'89': 'Prague' ,\
						'90': 'Episkopi' ,\
						'91': 'Ankara' ,\
						'92': 'Frankfurt/Main (RAFC)' ,\
						'93': 'London (WAFC)' ,\
						'94': 'Copenhagen' ,\
						'95': 'Rota' ,\
						'96': 'Athens' ,\
						'97': 'European Space Agency (ESA)' ,\
						'98': 'European Centre for Medium Range Weather Forecasts (ECMWF) (RSMC)' ,\
						'99': 'De Bilt' ,\
						'110': 'Hong Kong' ,\
						'160': 'US NOAA/NESDIS' ,\
						'210': 'Frascati (ESA/ESRIN)' ,\
						'211': 'Lanion' ,\
						'212': 'Lisboa' ,\
						'213': 'Reykjavik' ,\
						'254': 'EUMETSAT Operation Centre'}
indicatorOfParameterDic= {'001':'Pressure: Pa',\
						'002':'Pressure reduced to MSL: Pa'  ,\
						'003':'Pressure tendency: Pa/s' ,\
						'004':'Potential vorticity: K*m**2/kg/s' ,\
						'005':'ICAO Standard Atmosphere reference height: m' ,\
						'006':'Geopotential: m**2/s**2' ,\
						'007':'Geopotential height: gpm' ,\
						'008':'Geometrical height: m' ,\
						'009':'Standard deviation of height: m' ,\
						'010':'Total ozone: Dobson' ,\
						'011':'Temperature: K' ,\
						'012':'Virtual temperature: K' ,\
						'013':'Potential temperature: K' ,\
						'014':'Pseudo-adiabatic potential temperature: K' ,\
						'015':'Maximum temperature: K' ,\
						'016':'Minimum temperature: K' ,\
						'017':'Dew-point temperature: K' ,\
						'018':'Dew-point depression (or deficit): K' ,\
						'019':'Lapse rate:K/m' ,\
						'020':'Visibility:m' ,\
						'021':'Radar spectra (1)' ,\
						'022':'Radar spectra (2)' ,\
						'023':'Radar spectra (3)' ,\
						'024':'Parcel lifted index (to 500 hPa): K' ,\
						'025':'Temperature anomaly: K' ,\
						'026':'Pressure anomaly: Pa' ,\
						'027':'Geopotential height anomaly: gpm' ,\
						'028':'Wave spectra (1)',\
						'029':'Wave spectra (2)' ,\
						'030':'Wave spectra (3)' ,\
						'031':'Wind direction: Degree true' ,\
						'032':'Wind speed: m/s' ,\
						'033':'u-component of wind: m/s' ,\
						'034':'v-component of wind: m/s' ,\
						'035':'Stream function: m**2/s' ,\
						'036':'Velocity potential: m**2/s' ,\
						'037':'Montgomery stream function: m**2/s' ,\
						'038':'Sigma coordinate vertical velocity: s**-1' ,\
						'039':'Vertical velocity: Pa/s' ,\
						'040':'Vertical velocity: m/s' ,\
						'041':'Absolute vorticity: s**-1' ,\
						'042':'Absolute divergence: s**-1' ,\
						'043':'Relative vorticity: s**-1' ,\
						'044':'Relative divergence: s**-1' ,\
						'045':'Vertical u-component shear: s**-1' ,\
						'046':'Vertical v-component shear: s**-1' ,\
						'047':'Direction of current:Degree true' ,\
						'048':'Speed of current:m/s' ,\
						'049':'u-component of current: m/s' ,\
						'050':'v-component of current: m/s' ,\
						'051':'Specific humidity: kg/kg' ,\
						'052':'Relative humidity: %' ,\
						'053':'Humidity mixing ratio: kg/kg' ,\
						'054':'Precipitable water: kg/m**2' ,\
						'055':'Vapor pressure: Pa' ,\
						'056':'Saturation deficit: Pa' ,\
						'057':'Evaporation: kg/m**2' ,\
						'058':'Cloud ice: kg/m**2' ,\
						'059':'Precipitation rate: kg/m**2/s' ,\
						'060':'Thunderstorm probability: %' ,\
						'061':'Total precipitation: kg/m**2' ,\
						'062':'Large scale precipitation: kg/m**2' ,\
						'063':'Convective precipitation: kg/m**2' ,\
						'064':'Snowfall rate water equivalent: kg/m**2/s' ,\
						'065':'Water equivalent of accumulated snow depth: kg/m**2' ,\
						'066':'Snow depth: m' ,\
						'067':'Mixed layer depth: m' ,\
						'068':'Transient thermocline depth: m' ,\
						'069':'Main thermocline depth: m' ,\
						'070':'Main thermocline anomaly: m' ,\
						'071':'Total cloud cover: %' ,\
						'072':'Convective cloud cover: %' ,\
						'073':'Low cloud cover: %' ,\
						'074':'Medium cloud cover: %' ,\
						'075':'High cloud cover: %' ,\
						'076':'Cloud water: kg/m**2' ,\
						'077':'Best lifted index (to 500 hPa) : K' ,\
						'078':'Convective snow: kg/m**2' ,\
						'079':'Large scale snow: kg/m**2' ,\
						'080':'Water temperature: K' ,\
						'081':'Land cover (1 = land, 0 = sea): Proportion' ,\
						'082':'Deviation of sea level from mean: m' ,\
						'083':'Surface roughness:m' ,\
						'084':'Albedo: %' ,\
						'085':'Soil temperature: K' ,\
						'086':'Soil moisture content: kg/m**2' ,\
						'087':'Vegetation: %' ,\
						'088':'Salinity: kg/kg' ,\
						'089':'Density: kg/m**3' ,\
						'090':'Water run-off: kg/m**2' ,\
						'091':'Ice cover (1 = ice, 0 = no ice): Proportion' ,\
						'092':'Ice thickness: m' ,\
						'093':'Direction of ice drift: Degree true' ,\
						'094':'Speed of ice drift: m/s' ,\
						'095':'u-component of ice drift: m/s' ,\
						'096':'v-component of ice drift: m/s' ,\
						'097':'Ice growth rate: m/s' ,\
						'098':'Ice divergence: s**-1' ,\
						'099':'Snow melt: kg/m**2' ,\
						'100':'Significant height of combined wind waves and swell: m' ,\
						'101':'Direction of wind waves: Degree true' ,\
						'102':'Significant height of wind waves: m' ,\
						'103':'Mean period of wind waves: s' ,\
						'104':'Direction of swell waves: Degree true' ,\
						'105':'Significant height of swell waves: m' ,\
						'106':'Mean period of swell waves: s' ,\
						'107':'Primary wave direction: Degree true' ,\
						'108':'Primary wave mean period: s' ,\
						'109':'Secondary wave direction: Degree true' ,\
						'110':'Secondary wave mean period: s' ,\
						'111':'Net short-wave radiation flux (surface): W/m**2' ,\
						'112':'Net long-wave radiation flux (surface): W/m**2' ,\
						'113':'Net short-wave radiation flux (top of atmosphere): W/m**2' ,\
						'114':'Net long-wave radiation flux (top of atmosphere): W/m**2' ,\
						'115':'Long-wave radiation flux: W/m**2' ,\
						'116':'Short-wave radiation flux: W/m**2' ,\
						'117':'Global radiation flux: W/m**2' ,\
						'118':'Brightness temperature:K' ,\
						'119':'Radiance (with respect to wave number): W/m/sr' ,\
						'120':'Radiance (with respect to wave length): W/m**3/sr' ,\
						'121':'Latent heat flux: W/m**2' ,\
						'122':'Sensible heat flux: W/m**2' ,\
						'123':'Boundary layer dissipation: W/m**2' ,\
						'124':'Momentum flux, u-component: N/m**2' ,\
						'125':'Momentum flux, v-component: N/m**2' ,\
						'126':'Wind mixing energy: J' ,\
						'127':'Image data'}
dataRepresentationTypeDic= { \
						'0': 'Latitude/longitude grid - equidistant cylindrical or Plate Carrée projection' ,\
						'1': 'Mercator projection' ,\
						'2': 'Gnomonic projection' ,\
						'3': 'Lambert conformal, secant or tangent, conic or bi-polar, projection' ,\
						'4': 'Gaussian latitude/longitude grid' ,\
						'5': 'Polar stereographic projection' ,\
						'6': 'Universal Transverse Mercator (UTM) projection' ,\
						'7': 'Simple polyconic projection' ,\
						'8': 'Albers equal-area, secant or tangent, conic or bi-polar, projection' ,\
						'9': "Miller's cylindrical projection" ,\
						'10': 'Rotated latitude/longitude grid' ,\
						'13': 'Oblique Lambert conformal, secant or tangent, conic or bi-polar, projection' ,\
						'14': 'Rotated Gaussian latitude/longitude grid' ,\
						'20': 'Stretched latitude/longitude grid' ,\
						'24': 'Stretched Gaussian latitude/longitude grid' ,\
						'30': 'Stretched and rotated latitude/longitude grids' ,\
						'34': 'Stretched and rotated Gaussian latitude/longitude grids' ,\
						'50': 'Spherical harmonic coefficients' ,\
						'60': 'Rotated spherical harmonic coefficients' ,\
						'70': 'Stretched spherical harmonics' ,\
						'80': 'Stretched and rotated spherical harmonic coefficients' ,\
						'90': 'Space view, perspective orthographic'}

class TransformValues(object):
	"""docstring for TransformValues"""
	def unsignedIntValues(self,data,step=3):
		values= ''
		for i in range(step):
			values+= '{0:08b}'.format(data[i])
		return int(values,2)

	def intValues(self,data,step=2):
		values='{0:08b}'.format(data[0])[1:]
		for i in range(1,step):
			values+= '{0:08b}'.format(data[i])
		values=int(values,2)*((-1)**int('{0:08b}'.format(data[0])[0]))
		return values

	# def degreesValues(self,data,step=3):
	# 	values='{0:08b}'.format(data[0])[1:]
	# 	for i in range(1,step):
	# 		values+= '{0:08b}'.format(data[i])
	# 	degrees=int(values,2)*((-1)**int('{0:08b}'.format(data[0])[0]))
	# 	return degrees

	def floatValues(self,data):
		S= int('{0:08b}'.format(data[0])[0])
		A= int('{0:08b}'.format(data[0])[1:],2)
		# B= TransformValues().unsignedIntValues(data[1:])
		B= int('{0:08b}'.format(data[1])+'{0:08b}'.format(data[2])+'{0:08b}'.format(data[3]),2)
		values=((-1)**S)*(2**-24)*(16**(A-64))*B
		return values

class ReadSection0(object):
	"""Indicator section : 'GRIB', length of message, GRIB edition number"""
	def __init__(self, data, start= 4):
		self.data = data
		self.start= start
		self.lengthOfGribMessage= TransformValues().unsignedIntValues(self.data[4:7])
		self.editionOfGrib=self.data[7]
class ReadSection1(object):
	"""Product definition section : Length of section, identification of the coded anlysis or forecast"""
	def __init__(self, data, start= 8):
		self.data = data
		self.start= start
		self.lengthOfSection= TransformValues().unsignedIntValues(self.data[self.start:self.start+3])
		self.section1List=[1]*(self.lengthOfSection)
		for i in range(self.lengthOfSection):
			self.section1List[i]= self.data[self.start+i]
		self.gribTablesVersionNum= self.section1List[3]
		self.identificationOfOriginatingOrGeneratingCenter= identificationOfOriginatingOrGeneratingCenterDic['{0:02}'.format(self.section1List[4])]
		self.generatingProcessIdentificationNumber= self.section1List[5]
		self.gridDefinition= self.section1List[6]
		self.flag= '{0:08b}'.format(self.section1List[7])
		self.flagOfSection2=bool(int(self.flag[0]))
		self.flagOfSection3=bool(int(self.flag[1]))
		self.indicatorOfParameter= indicatorOfParameterDic['{0:03}'.format(self.section1List[8])]
		self.indicatorOfTypeOfLevel= self.section1List[9]
		if self.indicatorOfTypeOfLevel in [100,103,105,107,109,111,113,115,119,125,160]:
			self.heightPressureEtcOfLevels= int('{0:08b}'.format(self.section1List[10])+'{0:08b}'.format(self.section1List[11]),2)
		else: self.heightPressureEtcOfLevels= self.section1List[10:12]
		self.yearOfCentury= self.section1List[12]
		self.month= self.section1List[13]
		self.day= self.section1List[14]
		self.hour= self.section1List[15]
		self.minute= self.section1List[16]
		self.indicatorOfUnitOfTimeRange= self.section1List[17]
		self.P1= self.section1List[18]
		self.P2= self.section1List[19]
		self.timeRangeIndicator= self.section1List[20]
		self.numberIncludedInAverage1= self.section1List[21]
		self.numberIncludedInAverage2= self.section1List[22]
		self.numberMissingFromAveragesOrAccumulations= self.section1List[23]
		self.centuryOfReferenceTimeOfData= self.section1List[24]
		self.sub_centerIdentification= self.section1List[25] 
		self.unitsDecimalScaleFactor= TransformValues().intValues(self.section1List[26:28])
		try:
			self.reserved= self.section1List[28:]
		except :
			pass



class ReadSection2(object):
	"""Grid description section (optional) : Length of section, grid geometry, as necessary"""
	def __init__(self, data, start):
		self.data = data
		self.start= start
		self.lengthOfSection= TransformValues().unsignedIntValues(self.data[self.start:self.start+3])
		self.section2List=[1]*(self.lengthOfSection)
		for i in range(self.lengthOfSection):
			self.section2List[i]= self.data[self.start+i]		
		self.NV= self.section2List[3]		
		self.PVorPL= self.section2List[4]
		self.dataRepresentationType= self.section2List[5]
		if self.dataRepresentationType==0:
			self.Ni= TransformValues().unsignedIntValues(self.section2List[6:8],2)
			self.Nj= TransformValues().unsignedIntValues(self.section2List[8:10],2)
			self.La1= TransformValues().intValues(self.section2List[10:13],3)
			self.Lo1= TransformValues().intValues(self.section2List[13:16],3)
			self.resolutionAndComponentFlags= '{0:08b}'.format(self.section2List[16])
			self.La2= TransformValues().intValues(self.section2List[17:20],3)
			self.Lo2= TransformValues().intValues(self.section2List[20:23],3)
			self.Di= TransformValues().unsignedIntValues(self.section2List[23:25],2)
			self.Dj= TransformValues().unsignedIntValues(self.section2List[25:27],2)
			self.scanningMode= '{0:08b}'.format(self.section2List[27])
			self.reservedSetToZero= self.section2List[28:32]
			try:
				self.reserved= self.section1List[32:]
			except:
				pass




class ReadSection3(object):
	"""Bit-map section : Length of section; the bit per grid point, placed in suitable sequence, indicates omission (bit 0) or inclusion (bit 1) of data at respective points"""
	def __init__(self, data, start):
		self.data = data
		self.start= start
		self.lengthOfSection= TransformValues().unsignedIntValues(self.data[self.start:self.start+3])

class ReadSection4(object):
	"""Binary data section : Length of section and data values"""
	def __init__(self, data, start):
		self.data = data
		self.start= start
		self.lengthOfSection= TransformValues().unsignedIntValues(self.data[self.start:self.start+3])
		self.section4List=[1]*(self.lengthOfSection)
		for i in range(self.lengthOfSection):
			self.section4List[i]= self.data[self.start+i]
		self.flag= '{0:08b}'.format(self.section4List[3])
		self.scaleFactor= TransformValues().intValues(self.section4List[4:6])
		self.referenceValue= TransformValues().floatValues(self.section4List[6:10])
		self.numberOfBitsContainingEachPackedValue= self.section4List[10]
		if self.flag[0]=='0' and self.flag[1]=='0':
			self.data= [1]*((self.lengthOfSection-12)/2)
			step= self.numberOfBitsContainingEachPackedValue/8
			for i,j in zip(range(len(self.data)),range(11,self.lengthOfSection,step)):
				self.data[i]= TransformValues().unsignedIntValues(self.section4List[j:j+step],step)
		elif self.flag[0]=='1' and self.flag[1]=='0':
			pass
		elif self.flag[0]=='0' and self.flag[1]=='1':
			pass
		elif self.flag[0]=='1' and self.flag[1]=='1':
			pass


class ReadSection5(object):
	"""End section : 7777"""
	def __init__(self, data, start):
		self.data = data
		self.start= start

														
						
class ReadGribData(object):
	"""docstring for ReadRadar"""
	def __init__(self,filename):
		self.filename= filename
		self.gribFile= open(self.filename,'rb')
		self.originalData= self.gribFile.read()
		if self.originalData[0:4].strip(b'\x00').decode('gbk')== 'GRIB':
			self.originalDataTuple= struct.unpack(str(len(self.originalData))+'B',self.originalData[:])
			self.section0= ReadSection0(self.originalDataTuple)
			self.section1= ReadSection1(self.originalDataTuple)
			if self.section1.flagOfSection2:
				self.section2= ReadSection2(self.originalDataTuple,8+self.section1.lengthOfSection)
				if self.section1.flagOfSection3:
					self.section3= ReadSection3(self.originalDataTuple,8+self.section1.lengthOfSection+self.section2.lengthOfSection)
					self.section4= ReadSection4(self.originalDataTuple,8+self.section1.lengthOfSection+self.section2.lengthOfSection+self.section3.lengthOfSection)
				else:
					self.section4= ReadSection4(self.originalDataTuple,8+self.section1.lengthOfSection+self.section2.lengthOfSection)
			elif self.section1.flagOfSection3:
				self.section3= ReadSection3(self.originalDataTuple,8+self.section1.lengthOfSection)
				self.section4= ReadSection4(self.originalDataTuple,8+self.section1.lengthOfSection+self.section3.lengthOfSection)
		self.data= np.array(self.section4.data)
		self.data.resize(self.section2.Ni,self.section2.Nj)
		self.data= (self.data*(2**self.section4.scaleFactor)+self.section4.referenceValue)/(10**self.section1.unitsDecimalScaleFactor)
		# self.data= self.data.astype(float)
		