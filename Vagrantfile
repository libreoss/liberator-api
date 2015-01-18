# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.define "liberator" do |liberator|
        liberator.vm.box = "debian"
        liberator.vm.box_url = "ftp://ftp.lugons.org/vagrant/debian-7.6.0-x86_64.box"
        liberator.vm.network :private_network, ip: "192.168.66.6"
        liberator.vm.provision :ansible do |ansible|
            ansible.playbook = "provision/liberator.yml"
            ansible.host_key_checking = false
            ansible.groups = {
                "vagrant" => ["liberator"],
            }
        end
    end
    config.vm.define "dokuwiki" do |dokuwiki|
        dokuwiki.vm.box = "debian"
        dokuwiki.vm.box_url = "ftp://ftp.lugons.org/vagrant/debian-7.6.0-x86_64.box"
        dokuwiki.vm.network :private_network, ip: "192.168.66.7"
        dokuwiki.vm.provision :ansible do |ansible|
            ansible.playbook = "provision/dokuwiki.yml"
            ansible.host_key_checking = false
            ansible.groups = {
                "vagrant" => ["dokuwiki"],
            }
        end
    end
end
