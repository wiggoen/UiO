from pylab import *

L40_source = loadtxt("outputs/L60_avg.txt")
L60_source = loadtxt("outputs/L60_avg.txt")
L100_source = loadtxt("outputs/L100_avg.txt")
L140_source = loadtxt("outputs/L140_avg.txt")

numprocs = 4.0

def L40(L40_source):
    L40_N = L40_source[:,0][0]
    L40_MCC = L40_source[:,1][0]
    L40_norm1 = 1.0/(L40_MCC)
    L40_norm2 = 1.0/(L40_N)
    L40_T = L40_source[:,2]
    L40_meanE = L40_source[:,3]*numprocs        # Mean energy
    L40_meanE2 = L40_source[:,4]      
    L40_meanM = L40_source[:,5]
    L40_meanM2 = L40_source[:,6]
    L40_mean_absM = L40_source[:,7]*numprocs    # Mean absolute magnetization
    L40_specificHeat = L40_source[:,8]          # Heat capacity, Cv
    L40_Susceptibility = L40_source[:,9]        # Susceptibility, Chi, X
    return L40_T, L40_meanE, L40_mean_absM, L40_specificHeat, L40_Susceptibility

def L60(L60_source):
    L60_N = L60_source[:,0][0]
    L60_MCC = L60_source[:,1][0]
    L60_norm1 = 1.0/(L60_MCC)
    L60_norm2 = 1.0/(L60_N)
    L60_T = L60_source[:,2]
    L60_meanE = L60_source[:,3]*numprocs
    L60_meanE2 = L60_source[:,4]
    L60_meanM = L60_source[:,5]     
    L60_meanM2 = L60_source[:,6]
    L60_mean_absM = L60_source[:,7]*numprocs
    L60_specificHeat = L60_source[:,8]
    L60_Susceptibility = L60_source[:,9]
    return L60_T, L60_meanE, L60_mean_absM, L60_specificHeat, L60_Susceptibility

def L100(L100_source):
    L100_N = L100_source[:,0][0]
    L100_MCC = L100_source[:,1][0]
    L100_norm1 = 1.0/(L100_MCC)
    L100_norm2 = 1.0/(L100_N)
    L100_T = L100_source[:,2]
    L100_meanE = L100_source[:,3]*numprocs
    L100_meanE2 = L100_source[:,4]
    L100_meanM = L100_source[:,5]       
    L100_meanM2 = L100_source[:,6]
    L100_mean_absM = L100_source[:,7]*numprocs
    L100_specificHeat = L100_source[:,8]
    L100_Susceptibility = L100_source[:,9]
    return L100_T, L100_meanE, L100_mean_absM, L100_specificHeat, L100_Susceptibility

def L140(L140_source):
    L140_N = L140_source[:,0][0]
    L140_MCC = L140_source[:,1][0]
    L140_norm1 = 1.0/(L140_MCC)
    L140_norm2 = 1.0/(L140_N)
    L140_T = L140_source[:,2]
    L140_meanE = L140_source[:,3]*numprocs
    L140_meanE2 = L140_source[:,4]
    L140_meanM = L140_source[:,5]     
    L140_meanM2 = L140_source[:,6]
    L140_mean_absM = L140_source[:,7]*numprocs
    L140_specificHeat = L140_source[:,8] 
    L140_Susceptibility = L140_source[:,9] 
    return L140_T, L140_meanE, L140_mean_absM, L140_specificHeat, L140_Susceptibility

# Energy, absolute magnetization, heat capacity and susceptibility
T40, E40, M40, Cv40, X40 = L40(L40_source)
T60, E60, M60, Cv60, X60 = L60(L60_source)
T100, E100, M100, Cv100, X100 = L100(L100_source)
T140, E140, M140, Cv140, X140 = L140(L140_source)

# Energy and magnetization
fig = figure(1)
subplot(211)
plot(T40, E40, T60, E60, T100, E100, T140, E140)
art = []
lgd = legend([r"$L$ = 40", r"$L$ = 60", r"$L$ = 100", r"$L$ = 140"], loc="upper left", bbox_to_anchor=(1, 1))
xlabel(r"Temperature, $\hat{T}$", fontsize = 16)  
ylabel(r"$\langle E/L^2 \rangle$", fontsize = 18)
tick_params(labelsize=14)
fig.set_tight_layout(True)

subplot(212)
plot(T40, M40, T60, M60, T100, M100, T140, M140)
art = []
lgd = legend([r"$L$ = 40", r"$L$ = 60", r"$L$ = 100", r"$L$ = 140"], loc="upper left", bbox_to_anchor=(1, 1))
xlabel(r"Temperature, $\hat{T}$", fontsize = 16)  
ylabel(r"$\langle |M|/L^2 \rangle$", fontsize = 18)
tick_params(labelsize=14)
fig.set_tight_layout(True)

savefig("plots/opE_EM.png", additional_artists=art, bbox_inches="tight")
show()

# Heat capacity and susceptibility
fig = figure(2)
subplot(211)
plot(T40, Cv40, T60, Cv60, T100, Cv100, T140, Cv140)
art = []
lgd = legend([r"$L$ = 40", r"$L$ = 60", r"$L$ = 100", r"$L$ = 140"], loc="upper left", bbox_to_anchor=(1, 1))
xlabel(r"Temperature, $\hat{T}$", fontsize = 16)  
ylabel(r"$\langle C_v \rangle$", fontsize = 18)
tick_params(labelsize=14)
fig.set_tight_layout(True)

subplot(212)
plot(T40, X40, T60, X60, T100, X100, T140, X140)
art = []
lgd = legend([r"$L$ = 40", r"$L$ = 60", r"$L$ = 100", r"$L$ = 140"], loc="upper left", bbox_to_anchor=(1, 1))
xlabel(r"Temperature, $\hat{T}$", fontsize = 16)  
ylabel(r"$\langle \chi \rangle$", fontsize = 18)
tick_params(labelsize=14)
fig.set_tight_layout(True)

savefig("plots/opE_CvX.png", additional_artists=art, bbox_inches="tight")
show()